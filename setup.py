#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""Setup logic for pip."""

from setuptools import setup

def get_long_description():
    with open('README.md', 'r') as readme_file:
        return readme_file.read()

setup(
    name='prespa',
    version='0.1-sloth',
    description='An implementation of algorithm ReSPA in Python',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='github.com/valdigleis/prespa',
    author='Valdigleis S Costa',
    author_email='valdigleis@gmail.com',
    license='MIT License',
    packages=[
        'prespa',
        'prespa.filters'
    ],
    entry_points={},
    zip_safe=False
)