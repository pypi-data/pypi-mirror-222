#!/usr/bin/env python

from setuptools import setup

version = '0.0.2'

setup(name='gs_sql',
      author='EvgeniBondarev',
      author_email='bondareff7@gmail.com',
      version=version,
      description='Ability to use SQL when working with GoogleSheetAPI',
      long_description="Ability to use SQL when working with GoogleSheetAPI",
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

