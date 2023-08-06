from __future__ import annotations

import itertools
from abc import ABC
from dataclasses import dataclass, field
from functools import partial
from typing import Iterable, Generic, TypeVar, Sized, TYPE_CHECKING, Collection, Literal, ClassVar, Callable

import numpy as np
import pandas as pd

from .df_utils import derive_categoricals
from .header import Header, ObservationSpec, Meta, FeatureSpec
from .util import mangle_arg_to_set, mangle_arg_with_bool_fallback, mangle_arg_to_list, mangle_arg_to_tuple, \
    symmetric_difference, intersection, assert_in, StringEnumeration

if TYPE_CHECKING:
    pass

MDConcept = str


class MDConcepts(StringEnumeration):
    Time = 'time'
    Object = 'object'
    Type = 'type'
    Label = 'label'

    base_columns = [Time, Object, Type, Label]


class MDExtensionConcepts(StringEnumeration):
    Index = 'series_index'

    extension_columns = [Index]
    combined_columns = MDConcepts.base_columns + extension_columns


def only_feature_columns(cols):
    return [c for c in cols if (c not in MDConcepts.base_columns) and (c not in MDExtensionConcepts.extension_columns)]


def project_on_feature_columns(df: pd.DataFrame):
    return df[only_feature_columns(df.columns)]


TimeseriesFeatureLabel = str
TimeseriesFeatureLabels = tuple[TimeseriesFeatureLabel, ...]

ObservationTypeType = str


class ObservationTypes(StringEnumeration):
    E: ObservationTypeType = 'E'
    M: ObservationTypeType = 'M'


ObservationTypeLabel = str
ObservationSpecIdentifier = tuple[ObservationTypeType, ObservationTypeLabel]

EventSpecLabel = str
MeasurementSpecLabel = str

TimeseriesSpecType = TypeVar('TimeseriesTypeType', bound='TimeseriesSpec')


class TimeseriesTypeMergeException(Exception):
    pass


class TimeseriesCollectionMergeException(Exception):
    pass


class MachineDataMergeException(Exception):
    pass


@dataclass(frozen=True, unsafe_hash=True, eq=True, repr=True, init=False)
class TimeseriesSpec(Iterable, Sized):
    type: ClassVar[ObservationTypeType]
    label: ObservationTypeLabel
    base: ObservationSpec
    features: TimeseriesFeatureLabels = field(init=False)
    display_names: TimeseriesFeatureLabels = field(init=False)

    def __init__(self, label: ObservationTypeLabel, spec: ObservationSpec) -> None:
        super().__init__()
        object.__setattr__(self, 'label', label)
        object.__setattr__(self, 'base', spec)
        object.__setattr__(self, 'features', tuple((f.name for f in spec)))
        object.__setattr__(self, 'display_names', tuple((f.print_name for f in spec)))

    def __iter__(self):
        return iter(self.features)

    def __len__(self):
        return len(self.features)

    @property
    def identifier(self) -> ObservationSpecIdentifier:
        return self.type, self.label

    def is_mergeable(self, other: TimeseriesSpec) -> bool:
        return (self.__class__ == other.__class__) and (self.type == other.type) and (self.label == other.label)

    def feature_intersection(self, other: TimeseriesSpec) -> list[str]:
        return [f for f in self.features if f in set(other.features)]

    def feature_symmetric_difference(self, other: TimeseriesSpec) -> tuple[list[str], list[str]]:
        return [f for f in self.features if f not in set(other.features)], [f for f in other.features if
                                                                            f not in set(self.features)]

    def project(self: TimeseriesSpecType, feature_selection: bool | str | Collection[str]) -> TimeseriesSpecType:
        feature_selection = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, feature_selection, if_true=self.features)
        assert all(f in self.features for f in feature_selection)
        return self.__class__(self.label, ObservationSpec.of(*(self.base[f] for f in feature_selection)))

    def merge(self: TimeseriesSpecType, other: TimeseriesSpecType) -> TimeseriesSpecType:
        assert self.is_mergeable(other)
        specs = list(self.base.features)
        for fspec in other.base:
            if fspec not in self.base:
                specs.append(fspec)
            elif self.base[fspec.name] != fspec:
                print('redefined', self.base, self.base[fspec.name], fspec.name)
                raise TimeseriesTypeMergeException
        return self.__class__(self.label, ObservationSpec.of(*specs))


@dataclass(frozen=True, init=False)
class EventTimeseriesSpec(TimeseriesSpec):
    type = ObservationTypes.E


@dataclass(frozen=True, init=False)
class MeasurementTimeseriesSpec(TimeseriesSpec):
    type = ObservationTypes.M


class TimeseriesSpecFactory:
    types = {ObservationTypes.E: EventTimeseriesSpec, ObservationTypes.M: MeasurementTimeseriesSpec}

    @classmethod
    def for_type(cls, arg: str) -> Callable[[ObservationTypeLabel, ObservationSpec], TimeseriesSpec]:
        return cls.types[arg]


TSSpec = TypeVar('TSSpec', bound=TimeseriesSpec)


@dataclass
class AbstractMachineDataTimeseries(Generic[TSSpec], ABC):
    timeseries_spec: TSSpec
    df: pd.DataFrame


@dataclass
class MachineDataTimeseries(AbstractMachineDataTimeseries[TSSpec]):
    objects: Collection[str]


@dataclass
class EventSeries(MachineDataTimeseries[EventTimeseriesSpec]):
    pass


@dataclass
class MeasurementSeries(MachineDataTimeseries[MeasurementTimeseriesSpec]):
    pass


TS = TypeVar('TS', bound=MachineDataTimeseries)

TTC = TypeVar('TTC', bound='TypedTimeseriesCollection')


class TypedTimeseriesCollection(Generic[TSSpec, TS], ABC):
    _ts_spec_cls: type[TSSpec] = None
    _ts_cls: type[TS] = None

    def __init__(self, timeseries_spec: TSSpec, df: pd.DataFrame) -> None:
        super().__init__()
        self.timeseries_spec: TSSpec = timeseries_spec
        self.df: pd.DataFrame = df
        self._object_map: dict[str, TS] = {}
        self._repopulate_internal_index()

    @property
    def observation_count(self) -> int:
        return len(self.df)

    @property
    def occurring_objects(self) -> set[str]:
        return self._occurring_objects

    @property
    def time_series_count(self) -> int:
        return len(self._occurring_objects)

    @property
    def object_map(self) -> dict[str, TS]:
        return self._object_map

    @property
    def feature_column_view(self):
        return self.df.loc[:, list(self.timeseries_spec.features)]

    @property
    def prefixed_feature_column_view(self):
        df = self.feature_column_view
        return df.rename(
            {c: self.timeseries_spec.type + '_' + self.timeseries_spec.label + '_' + c for c in df.columns},
            inplace=False)

    def _repopulate_internal_index(self):
        self._internal_index = pd.Series(self.df.index, index=self.df[MDConcepts.Object])
        self._occurring_objects = set(self._internal_index.index)
        self._object_map = {obj: self.view(obj) for obj in self._occurring_objects}

    def _check_ts_features(self):
        return set(self.timeseries_spec.features) <= set(self.df.columns)

    def _mk_timeseries_view(self, timeseries_spec, objs) -> TS:
        df = self.df.loc[self._internal_index.loc[objs]]
        return self._ts_cls(timeseries_spec, df, set(df[MDConcepts.Object]))

    def _update_timeseries_spec(self, timeseries_spec: TSSpec = None) -> None:
        self.timeseries_spec = self._derive_timeseries_spec() if timeseries_spec is None else timeseries_spec
        assert self._check_ts_features()

    def _derive_timeseries_spec(self) -> TSSpec:
        current_features = only_feature_columns(self.df.columns)
        from .extensions import metadata

        specs: list[FeatureSpec] = []
        for f in current_features:
            fdt = metadata.get_type(self.df.loc[:, f])
            long_name = f
            if f in self.timeseries_spec.base:
                fspec: FeatureSpec = self.timeseries_spec.base[f]
                long_name = fspec.print_name
            specs.append(FeatureSpec(f, long_name, fdt))

        return self._ts_spec_cls(self.timeseries_spec.label, ObservationSpec(*specs))

    def update_index(self):
        self._repopulate_internal_index()

    def fit_to_data(self) -> None:
        self._update_timeseries_spec()
        self.update_index()

    def view(self, objs: str | list[str] | slice) -> TS:
        objs = slice(None) if objs is None else objs
        return self._mk_timeseries_view(self.timeseries_spec, objs)

    def __str__(self):
        return f'TimeseriesCollection(spec={self.timeseries_spec}, #obs={self.observation_count}, #objects={len(self.occurring_objects)})'

    def __repr__(self) -> str:
        return str(self)

    def merge(self: TTC, other: TTC,
              axis: Literal['horizontal', 'vertical'] = 'vertical') -> TTC:
        assert axis in {'horizontal', 'vertical'}
        if axis == 'horizontal':
            assert self.timeseries_spec.is_mergeable(other.timeseries_spec)
            ov = self.timeseries_spec.feature_intersection(other.timeseries_spec)
            if ov:
                assert self.df.loc[:, ov].equals(
                    other.df.loc[:, ov])  # np.array_equal(self.df.loc[:, ov].values, other.df.loc[:, ov].values)
            _, new_fs = self.timeseries_spec.feature_symmetric_difference(other.timeseries_spec)
            if new_fs:
                assert self.df[MDConcepts.Time].equals(other.df[MDConcepts.Time])
                df = pd.concat([self.df, other.df.loc[:, new_fs]], axis='columns', copy=True)
                return self.__class__(self.timeseries_spec.merge(other.timeseries_spec), df)
            return self
        elif axis == 'vertical':
            assert self.timeseries_spec == other.timeseries_spec
            df = pd.concat([self.df, other.df], axis='index', ignore_index=True, copy=True)
            df.sort_values(MDConcepts.Time, ignore_index=True, inplace=True)
            return self.__class__(self.timeseries_spec, df)

    @classmethod
    def lifted_merge(cls: type[TTC], tscs: dict[str, TTC], o_tscs: dict[str, TTC],
                     axis: Literal['horizontal', 'vertical'] = 'vertical') -> dict[str, TTC]:
        assert axis in {'horizontal', 'vertical'}
        ov = intersection(tscs.keys(), o_tscs.keys())
        s1, s2 = symmetric_difference(tscs.keys(), o_tscs.keys())
        res = {e: tscs[e] for e in s1} | {e: tscs[e].merge(o_tscs[e], axis=axis) for e in ov}
        if axis == 'horizontal':
            return res
        elif axis == 'vertical':
            return res | {e: o_tscs[e] for e in s2}


class EventTimeseriesCollection(TypedTimeseriesCollection[EventTimeseriesSpec, EventSeries]):
    _ts_spec_cls = EventTimeseriesSpec
    _ts_cls = EventSeries


class MeasurementTimeseriesCollection(TypedTimeseriesCollection[MeasurementTimeseriesSpec, MeasurementSeries]):
    _ts_spec_cls = MeasurementTimeseriesSpec
    _ts_cls = MeasurementSeries


ETSType = TypeVar('ETSType', bound=TimeseriesSpec)
MTSType = TypeVar('MTSType', bound=TimeseriesSpec)

ETS = TypeVar('ETS', bound=MachineDataTimeseries)
MTS = TypeVar('MTS', bound=MachineDataTimeseries)

ETSC = TypeVar('ETSC', bound=TypedTimeseriesCollection)
MTSC = TypeVar('MTSC', bound=TypedTimeseriesCollection)


class TimeseriesCollectionFactory:
    types = {ObservationTypes.E: EventTimeseriesCollection, ObservationTypes.M: MeasurementTimeseriesCollection}

    @classmethod
    def for_type(cls, timeseries_spec: TimeseriesSpec) -> Callable[[pd.DataFrame], TypedTimeseriesCollection]:
        if isinstance(timeseries_spec, EventTimeseriesSpec):
            return partial(cls.types[ObservationTypes.E], timeseries_spec)
        elif isinstance(timeseries_spec, MeasurementTimeseriesSpec):
            return partial(cls.types[ObservationTypes.M], timeseries_spec)


AMD = TypeVar('AMD', bound='AbstractMachineData')


class AbstractMachineData(Generic[ETSType, MTSType, ETS, MTS, ETSC, MTSC], ABC):
    _etsc_cls: type[ETSC] = None
    _mtsc_cls: type[MTSC] = None

    def __init__(self, meta: Meta, events: Iterable[ETSC],
                 measurements: Iterable[MTSC],
                 index_frame: pd.DataFrame = None) -> None:
        self._index_frame: pd.DataFrame = index_frame
        self.meta: Meta = meta
        self.event_specs: dict[EventSpecLabel, ETSType]
        self.measurement_specs: dict[MeasurementSpecLabel, MTSType]
        self.event_series: dict[EventSpecLabel, ETSC] = {etc.timeseries_spec.label: etc for etc in events}
        self.measurement_series: dict[MeasurementSpecLabel, MTSC] = {mtc.timeseries_spec.label: mtc for mtc in
                                                                     measurements}
        self._repopulate_maps()

    @property
    def header(self):
        return Header(self.meta, {e: tspec.base for e, tspec in self.event_specs.items()},
                      {m: tspec.base for m, tspec in self.measurement_specs.items()})

    @property
    def index_frame(self) -> pd.DataFrame:
        if self._index_frame is None:
            self.recalculate_index()
        return self._index_frame

    @index_frame.setter
    def index_frame(self, value: pd.DataFrame):
        self._index_frame = value

    @property
    def occurring_objects(self) -> set[str]:
        return self._occurring_objects

    @property
    def observation_count(self) -> int:
        return len(self.index_frame)

    @property
    def series_containers(self) -> list[ETSC | MTSC]:
        return list(self.event_series.values()) + list(self.measurement_series.values())

    @classmethod
    def from_series(cls: type[AMD], events: Iterable[ETSC],
                    measurements: Iterable[MTSC], lazy_index_creation=True, meta: Meta = Meta()) -> AMD:
        md = cls(meta, events, measurements)
        if not lazy_index_creation:
            md.recalulate_index()
        return md

    def recalculate_index(self, override_categorical_types=True, sort_by_time=True, **kwargs):
        self._index_frame = build_shared_index(self.series_containers,
                                               override_categorical_types=override_categorical_types,
                                               sort_by_time=sort_by_time, **kwargs)

    def _repopulate_maps(self):
        self.event_specs = {es.timeseries_spec.label: es.timeseries_spec for es in
                            self.event_series.values()}
        self.measurement_specs = {ms.timeseries_spec.label: ms.timeseries_spec for ms in
                                  self.measurement_series.values()}
        self._occurring_objects = set(self.index_frame[MDConcepts.Object])

    def fit_to_data(self, recreate_index=False):
        for tsc in self.iter_all_timeseries():
            # retain only the rows that are referenced in the overall index
            if not recreate_index:
                tsc.df = tsc.df.filter(items=self.index_frame.index, axis=0)
            tsc.fit_to_data()

        if recreate_index:
            self.recalculate_index()
        else:
            mask = pd.Series(False, index=self.index_frame.index)
            for tsc in self.iter_all_timeseries():
                mask |= self.index_frame.index.isin(tsc.df.index)
            self.index_frame = self.index_frame.loc[mask]

        self._repopulate_maps()

    def iter_all_timeseries(self) -> Iterable[TypedTimeseriesCollection]:
        return itertools.chain(self.event_series.values(), self.measurement_series.values())

    def create_joined_df(self, event_series_labels: Iterable[EventSpecLabel] | bool = None,
                         measurement_series_labels: Iterable[MeasurementSpecLabel] | bool = None,
                         prefix_columns_to_avoid_collisions=True):
        event_keys = self.event_specs.keys()
        esl = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, event_series_labels,
                                            if_true=event_keys,
                                            rm_duplicates=True, preserve_order=True)
        assert_in(esl, event_keys)
        measurement_keys = self.measurement_specs.keys()
        msl = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, measurement_series_labels,
                                            if_true=measurement_keys,
                                            rm_duplicates=True, preserve_order=True)
        assert_in(msl, measurement_keys)
        return pd.concat([self.index_frame] + [
            tsc.prefixed_feature_column_view if prefix_columns_to_avoid_collisions else tsc.feature_column_view for
            tsc in self.series_containers], axis='columns', copy=False)

    def create_index_view(self, typ: ObservationTypeType = None, types: Collection[ObservationTypeType] = None,
                          obj: str = None, objs: Iterable[str] = None,
                          label: ObservationTypeLabel = None,
                          labels: Iterable[ObservationTypeLabel] = None) -> pd.DataFrame:
        assert typ is None or types is None
        assert obj is None or objs is None
        assert label is None or labels is None

        mask = pd.Series(True, index=self.index_frame.index)
        if obj is not None:
            mask &= (self.index_frame[MDConcepts.Object] == obj)
        elif objs is not None:
            mask &= (self.index_frame[MDConcepts.Object].isin(mangle_arg_to_set(objs)))
        if label is not None:
            mask &= (self.index_frame[MDConcepts.Label] == label)
        elif labels is not None:
            mask &= (self.index_frame[MDConcepts.Label].isin(mangle_arg_to_set(labels)))
        if typ is not None:
            mask &= (self.index_frame[MDConcepts.Type] == typ)
        elif types is not None:
            mask &= (self.index_frame[MDConcepts.Type].isin(mangle_arg_to_set(typ)))

        return self.index_frame.loc[mask]

    def project(self: AMD,
                measurement_feature_selection: dict[
                    MeasurementSpecLabel, bool | Collection[TimeseriesFeatureLabel]] = None,
                event_feature_selection: dict[EventSpecLabel, bool | Collection[TimeseriesFeatureLabel]] = None,
                project_underlying_dfs=False, copy_underlying_dfs=False) -> AMD:
        if measurement_feature_selection is None:
            measurement_feature_selection = {}
        if event_feature_selection is None:
            event_feature_selection = {}
        ms = []
        for m, fs in measurement_feature_selection.items():
            fs = mangle_arg_with_bool_fallback(mangle_arg_to_list, fs,
                                               if_true=self.measurement_specs[m].features,
                                               preserve_order=True)
            mtc = self.measurement_series[m]
            tspec = mtc.timeseries_spec.project(fs)
            df = mtc.df.loc[:, MDConcepts.base_columns + list(tspec.features)] if project_underlying_dfs else mtc.df
            if copy_underlying_dfs:
                df = df.copy()
            ms.append(self._mtsc_cls(tspec, df))
        es = []
        for m, fs in event_feature_selection.items():
            fs = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, event_feature_selection,
                                               if_true=self.event_specs.keys(), preserve_order=True)
            etc = self.event_series[m]
            tspec = etc.timeseries_spec.project(fs)
            df = etc.df.loc[:, MDConcepts.base_columns + list(tspec.features)] if project_underlying_dfs else etc.df
            if copy_underlying_dfs:
                df = df.copy()
            es.append(self._etsc_cls(tspec, df))

        index_view = self.create_index_view(
            labels=itertools.chain(measurement_feature_selection.keys(), event_feature_selection.keys()))
        if copy_underlying_dfs:
            index_view = index_view.copy()
        return self.__class__(self.meta, es, ms, index_frame=index_view)

    def is_mergeable(self, other: AbstractMachineData):
        if self.__class__ != other.__class__:
            return False
        for e, et in self.event_specs.items():
            if o_et := other.event_specs.get(e):
                if not et.is_mergeable(o_et):
                    return False
        for m, mt in self.measurement_specs.items():
            if o_mt := other.measurement_specs.get(m):
                if not mt.is_mergeable(o_mt):
                    return False
        return True

    def merge(self: AMD, other: AMD,
              axis: Literal['horizontal', 'vertical'] = 'horizontal') -> AMD:
        result = self.merge_series(other.event_series, other.measurement_series, axis=axis)
        result.meta = self.meta.merge(other.meta)
        return result

    def merge_series(self, event_series: dict[EventSpecLabel, ETSC],
                     measurement_series: dict[MeasurementSpecLabel, MTSC],
                     axis: Literal['horizontal', 'vertical'] = 'horizontal') -> AMD:
        assert axis in {'horizontal', 'vertical'}
        recalc_index = axis == 'vertical'  # TODO actually detect if index changed #or (tsc. for tsc in event_series.values())
        if event_series is None:
            event_series = {}
        if measurement_series is None:
            measurement_series = {}
        es: dict[str, ETSC] = self._etsc_cls.lifted_merge(self.event_series, event_series, axis=axis)
        ms: dict[str, MTSC] = self._mtsc_cls.lifted_merge(self.measurement_series, measurement_series, axis=axis)
        if recalc_index:
            return self.__class__(self.meta, es.values(), ms.values())
        else:
            return self.__class__(self.meta, es.values(), ms.values(), self.index_frame)

    def get_event_series_collection(self, label: EventSpecLabel) -> ETSC:
        return self.event_series[label]

    def get_measurement_series_collection(self, label: MeasurementSpecLabel) -> MTSC:
        return self.measurement_series[label]

    def view_measurement_series(self, label: MeasurementSpecLabel, objs: str | list[str] | slice = slice(None),
                                **kwargs) -> MTS:
        return self.measurement_series[label].view(objs=objs)

    def view_event_series(self, label: EventSpecLabel, objs: str | list[str] | slice = slice(None),
                          **kwargs) -> ETS:
        return self.event_series[label].view(objs=objs)

    def summary(self):
        first = min(self.index_frame[MDConcepts.Time])
        last = max(self.index_frame[MDConcepts.Time])
        return f'#Observations: {self.observation_count} between {first} and {last}.' + '\n' + f'#Objects: {len(self.occurring_objects)}' + '\n' + f'#Event Specs: {len(self.event_specs)}' + '\n' + f'#Measurement Specs: {len(self.measurement_specs)}'

    def __str__(self):
        def spec_strings(specs_dict):
            return '\n'.join([f'\t{l}: {", ".join(tspec.features)}' for l, tspec in specs_dict.items()])

        especs = spec_strings(self.event_specs)
        mspecs = spec_strings(self.measurement_specs)
        objs = ' ' + ', '.join(self.occurring_objects)
        return 'MachineData {' + '\n' + 'Event Specs:' + (
            '\n' + especs if especs != "" else "[]") + '\n' + 'Measurement Specs:' + (
            '\n' + mspecs if mspecs != "" else "[]") + '\n' + 'Objects:' + objs + '\n' + f'Observations: {self.observation_count}' + '\n' + '}'

    def __repr__(self):
        return str(self)


class MachineData(AbstractMachineData[
                      EventTimeseriesSpec, MeasurementTimeseriesSpec, EventSeries, MeasurementSeries, EventTimeseriesCollection, MeasurementTimeseriesCollection]):
    _etsc_cls = EventTimeseriesCollection
    _mtsc_cls = MeasurementTimeseriesCollection


def build_shared_index(series: Iterable[TypedTimeseriesCollection], index_cols=None,
                       override_categorical_types=True,
                       sort_by_time=False):
    if index_cols is None:
        index_cols = MDConcepts.base_columns
    series = list(series)
    lengths = [len(tsc.df) for tsc in series]
    orig_idx_ranges = np.empty(len(lengths) + 1, dtype=int)
    np.cumsum(lengths, out=orig_idx_ranges[1:])
    orig_idx_ranges[0] = 0

    frame = pd.concat((tsc.df[index_cols] for tsc in series), ignore_index=True, join='inner',
                      copy=False)

    if sort_by_time:
        sorted_idx = np.argsort(frame[MDConcepts.Time].values)
        frame = frame.iloc[sorted_idx]
        frame.reset_index(drop=True, inplace=True)
        rev = np.empty_like(sorted_idx)
        rev[sorted_idx] = np.arange(len(sorted_idx))
        for tsc, start, end in zip(series, orig_idx_ranges[:-1], orig_idx_ranges[1:]):
            tsc.df.index = pd.Index(rev[start:end])
            tsc.update_index()
    else:
        for tsc, start, end in zip(series, orig_idx_ranges[:-1], orig_idx_ranges[1:]):
            tsc.df.index = pd.RangeIndex(start, end)
            tsc.update_index()

    cats = derive_categoricals(frame, [MDConcepts.Object, MDConcepts.Type, MDConcepts.Label])
    frame = frame.astype(cats, copy=False)
    if override_categorical_types:
        for tsc in series:
            tsc.df = tsc.df.astype(cats, copy=False)
    return frame
