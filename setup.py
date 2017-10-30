#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

about = {}
with open(os.path.join(os.path.dirname(__file__), "pyls_isort",
                       "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    url=about['__uri__'],
    author=about['__author__'],
    author_email=about['__email__'],
    license=about['__license__'],
    platforms="Any",
    packages=find_packages(),
    provides=['pyls_isort'],
    install_requires=['python-language-server', 'isort'],
    entry_points={
        'pyls': ['pyls_isort = pyls_isort.plugin'],
    },
)
