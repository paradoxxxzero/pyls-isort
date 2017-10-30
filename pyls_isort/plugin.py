import os

from isort import SortImports
from pyls import hookimpl


def sort(document, override=None):
    source = override or document.source
    sorted_source = SortImports(
        file_contents=source,
        settings_path=os.path.dirname(os.path.abspath(document.path))
    ).output
    if source == sorted_source:
        return
    return [{
        'range': {
            'start': {
                'line': 0,
                'character': 0
            },
            'end': {
                'line': len(document.lines),
                'character': 0
            }
        },
        'newText': sorted_source
    }]


@hookimpl(hookwrapper=True)
def pyls_format_document(document):
    outcome = yield
    results = outcome.get_result()
    if results:
        newResults = sort(document, results[0]['newText'])
    else:
        newResults = sort(document)

    if newResults:
        outcome.force_result(newResults)


@hookimpl(hookwrapper=True)
def pyls_format_range(document, range):
    outcome = yield
    results = outcome.get_result()
    if results:
        newResults = sort(document, results[0]['newText'])
    else:
        newResults = sort(document)

    if newResults:
        outcome.force_result(newResults)
