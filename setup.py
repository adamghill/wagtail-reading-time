#!/usr/bin/env python
"""
Installs the Wagtail readingtime plugin which displays an approximation of
how long it will take a user to read the text input into a rich text field.
"""

from setuptools import setup, find_packages

setup(name='wagtail-readingtime',
      version='1.0.0b',
      description='Determine approximate reading time of a piece of text.',
      url='https://github.com/vixdigital/wagtail-reading-time',
      author='VIX Digital',
      author_email='info@vix.digital',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'wagtail>=2.0',
      ],
      zip_safe=False)
