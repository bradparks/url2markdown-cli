#!/usr/bin/env python
#coding: utf-8

import os

from unittest import TextTestRunner

'''
The try statement is used to add python 2.6 support.
The unittest in python 2.6 doesn't have the loader function so
if the ImportError is thrown, it will switch and import unittest2
which is a module that has backported the 2.7 unittest to older
versions of python.
'''
try:
    from unittest import loader
except ImportError:
    from unittest2 import loader

test_path = os.path.join(os.path.dirname(__file__), 'tests')
test_loader = loader.TestLoader()

TextTestRunner(verbosity = 2).run(test_loader.discover(test_path))

