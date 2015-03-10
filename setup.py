#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'magnusknutas'

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "restedorm",
    version = "0.0.1",
    author = "Magnus Knutas",
    author_email = "magnus@thefarm.se",
    description = "A restful orm hook, inspired by django-orm",
    license = "BSD",
    keywords = "Restful ORM Django-rest-framework DRF",
    url = "https://github.com/MagnusKnutas/restedorm/",
    packages=['restedorm'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)