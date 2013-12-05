#!/usr/bin/env python

from setuptools import setup

setup(name='logpurge',
      version=0.1,
      description='Logarithmically purge data',
      author='Nick Tzaperas',
      author_email='nick@nijotz.com',
      url='http://github.com/nijotz/logpurge',
      packages=['logpurge'],
      entry_points = {
        'console_scripts': ['logpurge = logpurge:main',]
      },
      test_suite='nose.collector',
      tests_require=['nose', 'scripttest'],
)
