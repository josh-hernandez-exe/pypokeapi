#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='pypokeapi',
    version='0.1.0',
    description='A Python wrapper for PokeAPI',
    author='Josh Hernandez',
    author_email='I.Am.Mr.Josh.Hernandez@gmail.com',
    url='https://github.com/josh-hernandez-exe/pypokeapi',
    packages=[
        'pypokeapi',
    ],
    package_dir={'pypokeapi': 'pypokeapi'},
    include_package_data=True,
    install_requires=[
        'requests==2.0.1', 'simplejson==3.3.1'
    ],
    license="GNU",
    zip_safe=False,
    keywords='pypokeapi',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)
