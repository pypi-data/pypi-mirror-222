"""
annotate object series (object-segments if extension specified) with input/output before/after events
design decisions:
    how to handle validity checking with dependence on segment extension
    permit multiple annotations of same type per object (object-segment)?
    permit missing annotations?
"""

from mdata.core.util import StringEnumeration

CSV_KEY = 'A'


class AnnotationTypes(StringEnumeration):
    Input = 'I'
    Output = 'O'
    csv_tuple_qualifiers = [(CSV_KEY, Input), (CSV_KEY, Output)]
    long_names = {Input: 'input', Output: 'output'}

