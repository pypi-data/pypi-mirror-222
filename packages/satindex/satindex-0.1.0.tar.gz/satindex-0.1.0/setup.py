#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number,
# edit satindex/__init__.py


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="satindex",
    extras_require={
        "dev": [
            "bandit",
            "black",
            "flake8",
            "flake8-bugbear",
            "flake8-comprehensions",
            "flake8-docstrings",
            "flake8-polyfill",
            "isort",
            "mypy",
            "pre-commit",
            "pylint",
            "pylint[prospector]",
            "radon",
            "safety",
        ],
    },
    tests_require=["pytest", "pytest-cov"],
    test_suite="tests",
    version=find_version("satindex", "__init__.py"),
    description="This package calculates several indexes based onn multiband satellite images.",
    long_description=readme + "\n\n",
    author="RWS Datalab",
    author_email="datalab.codebase@rws.nl",
    url="https://gitlab.com/rwsdatalab/rwsdatalab/public/codebase/image/satindex",
    packages=["satindex"],
    include_package_data=True,
    package_data={"satindex": ["py.typed"]},
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="satindex",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        "numpy",
        "rasterio",
    ],
    setup_requires=[
        # dependency for `python setup.py test`
        "pytest-runner",
        # dependencies for `python setup.py build_sphinx`
        # "sphinx",
        # "sphinxcontrib-pdfembed @ https://github.com/SuperKogito/sphinxcontrib-pdfembed",
        # "sphinx_rtd_theme",
    ],
)
