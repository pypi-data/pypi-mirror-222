from __future__ import annotations

from typing import TypedDict, Any

import numpy as np
import pandas as pd

from .df_utils import derive_categoricals
from .extensions import metadata
from .header import create_header_from_raw, ObservationSpec, convert_header_to_raw
from .machine_data_def import MDConcepts, EventTimeseriesCollection, MeasurementTimeseriesCollection, MachineData, \
    TimeseriesCollectionFactory, TimeseriesSpecFactory


def gen_feature_column_names(n):
    return [f'f_{i}' for i in range(1, n + 1)]


class FeatureMetadata(TypedDict, total=False):
    data_type: str
    print_name: str


RawBaseFeatureSpec = str
RawMetadataFeatureSpec = dict[str, FeatureMetadata]
RawObservationSpecs = dict[str, list[RawBaseFeatureSpec | RawMetadataFeatureSpec]]


class RawAnnotationSpecs(TypedDict, total=True):
    input: RawObservationSpecs
    output: RawObservationSpecs


class RawHeaderSpec(TypedDict, total=False):
    extensions: list[str]
    event_specs: RawObservationSpecs
    measurement_specs: RawObservationSpecs
    annotation_specs: RawAnnotationSpecs
    metadata: dict[str, Any]


RawDataType = pd.DataFrame


def convert_to_raw_header(md: MachineData) -> RawHeaderSpec:
    return convert_header_to_raw(md.header)


def convert_to_raw_data(md: MachineData) -> RawDataType:
    max_features = max(map(lambda md_timeseries: len(md_timeseries.timeseries_spec), md.iter_all_timeseries()))
    # dfs = [pd.DataFrame(tsc.df[base_machine_data_columns + list(tsc.timeseries_type.features)], copy=False) for tsc in
    #       md.iter_all_timeseries()]
    # for df, tsc in zip(dfs, md.iter_all_timeseries()):
    #    df.columns = base_machine_data_columns + gen_feature_column_names(len(tsc.timeseries_type.features))
    # res = md.index_frame.join((df.drop(base_machine_data_columns, axis=1) for df in dfs), how='inner')
    # TODO CHANGE BACK

    res = pd.DataFrame(md.index_frame, copy=True)  # .reindex(columns=))
    res[gen_feature_column_names(max_features)] = np.NAN

    # res.columns = base_raw_machine_data_columns + gen_feature_column_names(max_features)
    for tsc in md.iter_all_timeseries():
        df = tsc.df
        cs = gen_feature_column_names(len(tsc.timeseries_spec.features))
        res.loc[df.index, cs] = df.loc[:, list(tsc.timeseries_spec.features)].values

    res.columns = MDConcepts.base_columns + gen_feature_column_names(max_features)
    # res = pd.concat(dfs, ignore_index=True, copy=False, verify_integrity=False, join='inner') # TODO check copying

    # res.sort_values(COLUMN_NAME_DICT[MDConcepts.Time], ascending=True, inplace=True)
    return res


def convert_to_raw_data_legacy(md: MachineData) -> RawDataType:
    max_features = max(map(lambda md_timeseries: len(md_timeseries.timeseries_spec), md.iter_all_timeseries()))
    rows = []
    for typed_timeseries in md.iter_all_timeseries():
        tt = typed_timeseries.timeseries_spec
        df = typed_timeseries.df
        for tup in df.itertuples(index=True):
            rows.append(
                [getattr(tup, MDConcepts.Time), getattr(tup, MDConcepts.Object), tt.type,
                 tt.label] + [getattr(tup, f)
                              for f in
                              tt.features if
                              f in df.columns])
    res = pd.DataFrame(rows, columns=(MDConcepts.base_columns + gen_feature_column_names(max_features)))
    res.sort_values(MDConcepts.Time, inplace=True)
    return res


def create_machine_data_from_raw(raw_data: RawDataType, raw_header: RawHeaderSpec):
    header = create_header_from_raw(raw_header)

    mdes, mdms = [], []

    categories = derive_categoricals(raw_data, [MDConcepts.Object, MDConcepts.Label, MDConcepts.Type])

    overall = pd.DataFrame(raw_data, columns=MDConcepts.base_columns, copy=True)
    overall = overall.astype(categories, copy=False)

    for group, idx in overall.groupby([MDConcepts.Type, MDConcepts.Label]).groups.items():
        tpy, label = group
        spec: ObservationSpec = header.lookup_spec(tpy, label)

        timeseries_type = TimeseriesSpecFactory.for_type(tpy)(label, spec)

        actual_feature_labels = timeseries_type.features
        feature_count = len(actual_feature_labels)
        placeholder_feature_labels = gen_feature_column_names(feature_count)
        df = pd.concat([overall.loc[idx, MDConcepts.base_columns], raw_data.loc[idx, placeholder_feature_labels]],
                       copy=True, axis=1).set_index(idx)
        # relevant_cols = list(base_machine_data_columns) + placeholder_feature_labels
        # df = pd.DataFrame(raw_data.loc[idx, relevant_cols], copy=True)
        # not a good idea in case of duplicates
        # df.set_index('time', inplace=True, verify_integrity=True, drop=False)
        renaming_dict = {old: new for old, new in zip(placeholder_feature_labels, actual_feature_labels)}
        df.rename(columns=renaming_dict, inplace=True)

        metadata.convert_df_inplace(df, {f.name: f.data_type for f in spec})

        ts_collection = TimeseriesCollectionFactory.for_type(timeseries_type)(df)
        if isinstance(ts_collection, EventTimeseriesCollection):
            mdes.append(ts_collection)
        elif isinstance(ts_collection, MeasurementTimeseriesCollection):
            mdms.append(ts_collection)

    placeholder_cols = list(set(overall.columns).difference(MDConcepts.base_columns))
    overall.drop(columns=placeholder_cols, inplace=True)

    return MachineData(header.meta, mdes, mdms, index_frame=overall)
