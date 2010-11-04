#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from setuptools import setup, find_packages
import sys, os

version = '.1'

setup(name='pygsm',
      version=version,
      description="",
      long_description="""\
PyGSM is a Free and Open Source library for interfacing with
GSM modems and handsets to send and receive SMS messages.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
        "pyserial",
        "pytz",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
