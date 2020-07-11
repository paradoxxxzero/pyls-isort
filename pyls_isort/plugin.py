import os

try:
    # isort<5
    from isort import SortImports

    def isort_sort(source, settings_path):
        return SortImports(
            file_contents=source,
            settings_path=settings_path,
        ).output

except ImportError:
    # isort=>5
    from isort import code
    from isort.settings import Config

    def isort_sort(source, settings_path):
        return code(source, config=Config(settings_path=settings_path))


from pyls import hookimpl


def sort(document, override=None):
    source = override or document.source
    sorted_source = isort_sort(
        source,
        os.path.dirname(os.path.abspath(document.path)),
    )
    if source == sorted_source:
        return
    return [{
        'range': {
            'start': {
                'line': 0,
                'character': 0,
            },
            'end': {
                'line': len(document.lines),
                'character': 0,
            },
        },
        'newText': sorted_source,
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
