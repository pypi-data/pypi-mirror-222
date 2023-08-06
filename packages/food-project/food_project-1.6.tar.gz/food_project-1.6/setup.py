#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='food_project',
    version='1.6',
    description='An example package.',
    long_description='Very tasty burger',
    long_description_content_type='text/x-rst',
    url='https://github.com/shuygena/food_project',
    author='Zukhra Khubieva & Vadim Petruhnenko \\ shuygena',
    author_email='hubieva123@icloud.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],

    entry_points={
        'console_scripts': [
            'food_project = food_project.cli:main',
        ]
    },
)