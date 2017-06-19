#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'six>=1.7.3',
    'toolz>=0.8.2',
]

test_requirements = [
    # TODO: put package test requirements here
    'coverage',
    'flake8',
    'pytest',
    'pytest-cov',
    'tox',
    'mock',
]

setup(
    name='pyresult',
    version='0.6.0',
    description="A Result pattern for python",
    long_description=readme + '\n\n' + history,
    author="Jindrich Kralevic Smitka",
    author_email='smitka.j@gmail.com',
    url='https://github.com/iodevs/pyresult',
    packages=[
        'pyresult',
    ],
    package_dir={'pyresult':
                 'pyresult'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='pyresult',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
