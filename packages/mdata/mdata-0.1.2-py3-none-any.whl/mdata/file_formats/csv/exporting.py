import csv
import io
import json
import os
import sys
from typing import Optional, TextIO

import yaml

from mdata.core import machine_data_def as mdd
from mdata.core import raw
from mdata.core.extensions import metadata, registry
from mdata.file_formats import io_utils
from .shared import mk_filename_pair, HeaderFormatLiterals, HeaderFileFormat, DictHeaderFormatLiterals


class UnsupportedWritingTarget(Exception):
    def __init__(self, arg) -> None:
        super().__init__(f'Cannot write to {arg} of type {type(arg)}.')


WritingTarget = str | os.PathLike[str] | TextIO | io.StringIO


def pad_lengths(lol: list[list[str]]):
    mlen = max(map(len, lol))
    return [l + [''] * (mlen - len(l)) for l in lol]


def write_raw_header(target: WritingTarget, header: raw.RawHeaderSpec):
    def write_into(into):
        writer = csv.writer(into)
        exts = header.get('extensions', [])
        use_metadata = 'metadata' in exts
        rows = []

        def all_specs():
            return zip([mdd.ObservationTypes.E, mdd.ObservationTypes.M],
                       [header['event_specs'].items(), header['measurement_specs'].items()])

        # add header row
        mlen = max(len(s) for typ, specs in all_specs() for _, s in specs)
        rows.append([mdd.MDConcepts.Type, mdd.MDConcepts.Label] + raw.gen_feature_column_names(mlen))

        for typ, specs in all_specs():
            rows += [[typ, label] + [f if type(f) is str else f['name'] for f in spec] for label, spec in specs]

        if len(exts) > 0:
            rows.append([registry.CSV_KEY] + [e for e in exts])

        if use_metadata:
            for typ, specs in all_specs():
                for label, spec in specs:
                    for f in spec:
                        if isinstance(f, raw.RawMetadataFeatureSpec):
                            if (pn := f.get('print_name')) is not None:
                                rows.append([metadata.CSV_KEY, 'print_name', typ, label, f, pn])
                            if (dt := f.get('data_type')) is not None:
                                rows.append([metadata.CSV_KEY, 'data_type', typ, label, f, dt])

        # TODO annotations
        writer.writerows(pad_lengths(rows))

    if isinstance(target, str | os.PathLike):
        io_utils.ensure_directory_exists(target)
        target = io_utils.ensure_ext(target, '.csv')
        with open(target, 'w', newline='', encoding='utf-8') as csvfile:
            write_into(csvfile)
    else:
        try:
            write_into(target)
        except Exception:
            tb = sys.exc_info()[2]
            raise UnsupportedWritingTarget(target).with_traceback(tb)


def write_raw_header_dict(target, header: raw.RawHeaderSpec, dict_header_format: DictHeaderFormatLiterals = 'json'):
    assert dict_header_format in {HeaderFileFormat.JSON, HeaderFileFormat.YAML}

    def write_into(into):
        pass

    if dict_header_format == HeaderFileFormat.JSON:
        def write_into(into):
            json.dump(header, into, indent=2)
    elif dict_header_format == HeaderFileFormat.YAML:
        def write_into(into):
            yaml.dump(header, into)

    if isinstance(target, str | os.PathLike):
        io_utils.ensure_directory_exists(target)
        target = io_utils.ensure_ext(target, '.json' if dict_header_format == HeaderFileFormat.JSON else '.yaml')
        with open(target, 'w') as file:
            write_into(file)
    else:
        try:
            write_into(target)
        except Exception:
            tb = sys.exc_info()[2]
            raise UnsupportedWritingTarget(target).with_traceback(tb)


def write_raw_data(target: WritingTarget, df: raw.RawDataType):
    if isinstance(target, str | os.PathLike):
        io_utils.ensure_directory_exists(target)
        target = io_utils.ensure_ext(target, '.csv')
    df.to_csv(target, index=False)


def write_machine_data(path: str | os.PathLike, md: mdd.MachineData, header_format: HeaderFormatLiterals = 'csv'):
    header_file, data_file = mk_filename_pair(path, header_format=header_format)
    write_machine_data_custom(header_file, data_file, md, header_format)


def write_machine_data_custom(header_target: Optional[WritingTarget], data_target: Optional[WritingTarget],
                              md: mdd.MachineData,
                              header_format: HeaderFormatLiterals):
    raw_header = raw.convert_to_raw_header(md)
    assert header_format in HeaderFileFormat
    if header_target is not None:
        if header_format == HeaderFileFormat.CSV:
            write_raw_header(header_target, raw_header)
        elif header_format in {HeaderFileFormat.JSON, HeaderFileFormat.YAML}:
            write_raw_header_dict(header_target, raw_header, dict_header_format=header_format)
    if data_target is not None:
        write_raw_data(data_target, raw.convert_to_raw_data(md))


def write_header_file(path: str | os.PathLike, md: mdd.MachineData, header_format: HeaderFormatLiterals = 'csv'):
    header_file, _ = mk_filename_pair(path, header_format=header_format)
    raw_header = raw.convert_to_raw_header(md)
    assert header_format in HeaderFileFormat
    if header_format == HeaderFileFormat.CSV:
        write_raw_header(header_file, raw_header)
    elif header_format in {HeaderFileFormat.JSON, HeaderFileFormat.YAML}:
        write_raw_header_dict(header_file, raw_header, dict_header_format=header_format)


def write_data_file(path: str | os.PathLike, md: mdd.MachineData):
    _, data_file = mk_filename_pair(path)
    write_raw_data(data_file, raw.convert_to_raw_data(md))
