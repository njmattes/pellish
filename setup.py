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
    long_description = f.read().decode('utf-8')
 
 
setup(
    name='pellish',
    packages=['pellish'],
    entry_points={
        'console_scripts': ['pellish = pellish.pellish:main']
    },
    license='GPLv3',
    version=version,
    description='Python command line application for generating Pell-like sequences.',
    long_description=long_description,
    author='Nathan Matteson',
    author_email='matteson@obstructures.org',
    url='',
)