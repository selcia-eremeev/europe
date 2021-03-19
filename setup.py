#!/usr/bin/env python
from setuptools import setup

with open("requirements.in") as r:
    req = r.read().splitlines()

setup(
    name="europe",
    version="1.0.0",
    author="Selcia Eremeev",
    packages=["europe"],
    package_data={"europe": ["py.typed"]},
    include_package_data=True,
    install_requires=req,
    zip_safe=False,
)