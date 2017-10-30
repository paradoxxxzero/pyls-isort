import os

from isort import SortImports
from pyls import hookimpl


def sort(document):
    source = document.source
    sorted_source = SortImports(
        file_contents=document.source,
        settings_path=os.path.dirname(os.path.abspath(document.path))
    ).output
    if source == sorted_source:
        return []

    return [{
        'range': {
            'start': {'line': 0, 'character': 0},
            'end': {'line': len(document.lines), 'character': 0}
        },
        'newText': sorted_source
    }]


@hookimpl
def pyls_format_document(document):
    return sort(document)


@hookimpl
def pyls_format_range(document, range):
    return sort(document)
