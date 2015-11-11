#!/usr/bin/env python
#coding: utf-8

import unittest
import url2markdown

class ArgumentParserTester(unittest.TestCase):

    def parse(self, *args):
        return self.parser.parse_args(args)

    def setUp(self):
        self.parser = url2markdown.parser

    def test_URL(self):
        url = "http://sample.org"
        parsed = self.parse(url)
        self.assertEqual(parsed.URL, url)
    
    def test_file(self):
        file = "sample.md"
        url = "http://sample.org"
        parsed = self.parse(url, "-O", file)
        self.assertEqual(parsed.file, file)
