#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup
 
 
version = re.search(
    '^__version__\s*=\s*\'(.*)\'',
    open('pellish/pellish.py').read(),
    re.M
    ).group(1)
 
with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')
 
 
setup(
    name='pellish',
    packages=['pellish'],
    entry_points={
        'console_scripts': ['pellish = pellish.pellish:main']
    },
    version=version,
    description='Python command line application for generating Pell-like sequences.',
    long_description=long_descr,
    author='Nathan Matteson',
    author_email='matteson@obstructures.org',
    url='',
)