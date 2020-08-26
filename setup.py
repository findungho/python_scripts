# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import dirname, join

with open(join(dirname("."), "VERSION"), "rb") as f:
    version = f.read().decode("ascii").strip()

setup(
    name="{pythons}",
    version=version,
    python_requires=">=3.7.0",
    long_description=__doc__,
    packages=find_packages(),
    py_modules=["{PACKAGE_NAME}"],
    include_package_data=True,
    zip_safe=False,
)
