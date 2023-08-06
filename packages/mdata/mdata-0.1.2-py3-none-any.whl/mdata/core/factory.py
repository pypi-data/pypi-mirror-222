from __future__ import annotations

import itertools
from collections.abc import Iterable
from typing import TypedDict

import pandas as pd

from mdata.core.header import ObservationSpec, Meta
from mdata.core.machine_data_def import MDConcepts, TimeseriesSpecFactory, only_feature_columns, \
    TimeseriesCollectionFactory, EventTimeseriesCollection, MachineData, MeasurementTimeseriesCollection, \
    ObservationTypes, build_shared_index, TypedTimeseriesCollection
from mdata.core.raw import create_machine_data_from_raw, RawHeaderSpec, RawDataType, RawMetadataFeatureSpec
from mdata.core.util import take_first


def ets_from_df(df: pd.DataFrame, **kwargs):
    return ts_from_df(df, type=ObservationTypes.E, **kwargs)


def mts_from_df(df: pd.DataFrame, **kwargs):
    return ts_from_df(df, type=ObservationTypes.M, **kwargs)


def ts_from_df(df: pd.DataFrame, specmeta: Iterable[RawMetadataFeatureSpec] = (), copy=False,
               **kwargs) -> TypedTimeseriesCollection:
    df = df.copy() if copy else df

    def match_spec_and_df(concept, col_idx):
        spec = kwargs.get(concept)
        if concept not in df.columns:
            assert spec is not None
            df.insert(col_idx, concept, spec)
        else:
            df_type = df.iloc[0][concept]
            assert spec is None or spec == df_type
            spec = df_type
        return spec

    if MDConcepts.Time in kwargs:
        spec_time = kwargs[MDConcepts.Time]
        if spec_time == 'artificial':
            from mdata.core import df_utils
            df.insert(0, MDConcepts.Time, df_utils.create_artificial_daterange(df))
    spec_object = match_spec_and_df(MDConcepts.Object, 1)
    spec_type = match_spec_and_df(MDConcepts.Type, 2)
    spec_label = match_spec_and_df(MDConcepts.Label, 3)

    tspec_cls = TimeseriesSpecFactory.for_type(spec_type)
    features = only_feature_columns(df.columns)

    specmeta = {take_first(fspec): fspec for fspec in specmeta}
    tt = tspec_cls(spec_label, ObservationSpec.from_raw([specmeta[f] if f in specmeta else f for f in features]))
    return TimeseriesCollectionFactory.for_type(tt)(df)


ObservationSeriesDef = TypedDict('ObservationSeriesDef',
                                 {'df': pd.DataFrame, MDConcepts.Object: str, MDConcepts.Time: str,
                                  MDConcepts.Label: str, 'specmeta': list[RawMetadataFeatureSpec]},
                                 total=False)


def machine_data_from_series(*series_defs: ObservationSeriesDef, meta: Meta = Meta(), sort_by_time=True, copy_dfs=False,
                             **kwargs) -> MachineData:
    ets, mts = [], []
    for sd in series_defs:
        assert 'df' in sd
        tsc = ts_from_df(**sd, copy=copy_dfs)
        if isinstance(tsc, EventTimeseriesCollection):
            ets.append(tsc)
        elif isinstance(tsc, MeasurementTimeseriesCollection):
            mts.append(tsc)

    index_frame = build_shared_index(itertools.chain(ets, mts), sort_by_time=sort_by_time, **kwargs)
    return MachineData(meta, ets, mts, index_frame)


def machine_data_from_df(df: RawDataType, header: RawHeaderSpec) -> MachineData:
    return create_machine_data_from_raw(df, header)
