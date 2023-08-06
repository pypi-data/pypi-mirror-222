#!/usr/bin/env python

from io import open
from setuptools import setup

version = '0.0.3'

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(name='gs_sql',
      author='EvgeniBondarev',
      author_email='bondareff7@gmail.com',
      version=version,
      description='Ability to use SQL when working with GoogleSheetAPI',
      long_description_content_type='text/markdown',
      long_description=readme,
      url='https://github.com/EvgeniBondarev/PyGoogleSheetAPI',
      download_url='https://github.com/EvgeniBondarev/PyGoogleSheetAPI/archive/refs/heads/main.zip'.format(
            version),
      license='Apache License, Version 2.0, see LICENSE file',
      classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
      ],
      zip_safe=False
    )

