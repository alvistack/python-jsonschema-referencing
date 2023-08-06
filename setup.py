# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='referencing',
    version='0.30.2',
    description='JSON Referencing + Python',
    author='Julian Berman',
    author_email='Julian+referencing@GrayVines.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: File Formats :: JSON',
        'Topic :: File Formats :: JSON :: JSON Schema',
    ],
    install_requires=[
        'attrs>=22.2.0',
        'rpds-py>=0.7.0',
    ],
    packages=[
        'referencing',
    ],
)
