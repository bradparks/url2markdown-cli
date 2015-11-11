#!/usr/bin/env python
#coding: utf-8

import unittest
import url2markdown.__main__ as url2markdown

class ConvertTester(unittest.TestCase):

    def test_raise_ConvertError(self):
        url = "not url"
        with self.assertRaises(url2markdown.ConvertError):
            url2markdown.convert(url)
    
    def test_correct_convert(self):
        url = "http://url2markdown.herokuapp.com/"
        converted = url2markdown.convert(url)
        self.assertEqual(converted,"""# url2markdown

This is a very simple web service that will take a given URL, and return a
Markdown representation of that page.

URL:

A [Kenneth Reitz](http://kennethreitz.org/) project.

[![Fork me on GitHub](https://s3.amazonaws.com/github/ribbons/forkme_right_dar
kblue_121621.png)](https://github.com/kennethreitz/url2markdown)

""")

