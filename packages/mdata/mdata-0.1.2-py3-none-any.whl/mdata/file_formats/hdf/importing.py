import pandas as pd

from mdata.core import factory
from mdata.core import machine_data_def as mdd
from mdata.core.header import Meta
from mdata.core.raw import RawMetadataFeatureSpec


class InvalidHeaderException(Exception): pass


def read_machine_data_h5(filename) -> mdd.MachineData:
    # ext = io_utils.ensure_ext(filename, '.h5', override_ext=False)

    with pd.HDFStore(filename, mode='r') as store:
        measurements, events = [], []
        rel_groups = next(store.walk('/'))[1]

        extensions = set()
        use_metadata = False
        if store.get_node('meta/extensions') is not None:
            extensions = set(store.get('meta/extensions'))
            use_metadata = 'metadata' in extensions

        metadata = {}
        if use_metadata and store.get_node('meta/metadata') is not None:
            metadata_df: pd.DataFrame = store.get('meta/metadata')
            for key, row in metadata_df.iterrows():
                value = row['value']
                metadata[str(key)] = value

        if use_metadata and store.get_node('meta/specs') is not None:
            specmeta = store.get('meta/specs')

            def get_meta(t, l):
                specmeta: pd.DataFrame
                results = specmeta.loc[
                    (specmeta[mdd.MDConcepts.Type] == t) & (specmeta[mdd.MDConcepts.Label] == l), ['feature',
                                                                                                   'print_name',
                                                                                                   'data_type']]
                specs = []
                for f, idx in results.groupby('feature').groups.items():
                    g = results.loc[idx][['print_name', 'data_type']]
                    if len(g) != 1:
                        raise InvalidHeaderException(f'Duplicate feature metadata for {f}.')
                    pn, dt = g.iloc[0]
                    specs.append(RawMetadataFeatureSpec({f: {'print_name': pn, 'data_type': dt}}))
                return specs

        meta = Meta(extensions, metadata)

        if 'events' in rel_groups:
            (path, groups, leaves) = next(store.walk('/events'))
            for label in leaves:
                key = '/'.join([path, label])
                df: pd.DataFrame = store.get(key)
                specs = get_meta(mdd.ObservationTypes.E, label) if use_metadata else ()
                ets = factory.ts_from_df(df, specmeta=specs)
                events.append(ets)
        if 'measurements' in rel_groups:
            (path, groups, leaves) = next(store.walk('/measurements'))
            for label in leaves:
                key = '/'.join([path, label])
                df: pd.DataFrame = store.get(key)
                specs = get_meta(mdd.ObservationTypes.M, label) if use_metadata else ()
                mts = factory.ts_from_df(df, specmeta=specs)
                measurements.append(mts)

        index_frame: pd.DataFrame = store.get('index')

        return mdd.MachineData(meta, events, measurements, index_frame=index_frame)
