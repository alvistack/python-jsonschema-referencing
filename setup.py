# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='referencing',
    version='0.36.2',
    description='JSON Referencing + Python',
    author_email='Julian Berman <Julian+referencing@GrayVines.com>',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: File Formats :: JSON',
        'Topic :: File Formats :: JSON :: JSON Schema',
    ],
    install_requires=[
        'attrs>=22.2.0',
        'rpds-py>=0.7.0',
        'typing-extensions>=4.4.0; python_version < "3.13"',
    ],
    packages=[
        'referencing',
    ],
)
