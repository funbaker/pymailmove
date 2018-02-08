# -*- coding: utf-8 -*-

import sys
import os
from setuptools import setup, find_packages

# make pymailmove available in path
sys.path.insert(0, os.path.abspath('.'))

import pymailmove

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pymailmove',
    version=pymailmove.__version__,
    description='Package for copying mail between different locations',
    long_description=readme,
    author='Stefan Becker',
    author_email='ich@funbaker.de',
    url='https://github.com/funbaker/pymailmove',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_required=['click'],
    entry_points={
        'console_scripts': [
            'pymailmove = pymailmove.cli:main'
        ]
    }
)
