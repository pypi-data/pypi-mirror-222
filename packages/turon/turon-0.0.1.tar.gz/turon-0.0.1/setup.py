#!/usr/bin/env python

from distutils.core import setup
from turon import __version__


setup(
    name='turon',
    version=__version__,
    description='Python iterface for turon.io',
    author='Scott Cruwys',
    author_email='scott@turon.io',
    url='https://ww.github.com/tryturon/turon-py',
    packages=['turon'],
)
