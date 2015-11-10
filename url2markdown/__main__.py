#!/usr/bin/env python
#coding: utf-8

import os
import sys
import requests
import argparse

__version__ = "1.0b"

parser = argparse.ArgumentParser(
                    prog="url2markdown", version=__version__,
                    description="Convert website to markdown from an url. "
                                "This script provided by http://url2markdown.herokuapp.com/")
parser.add_argument("URL",action="store",
                    help="An URL of website.")
parser.add_argument("-O",action="store",dest="file",
                    help="Save markdown to file.")

class ConvertError(Exception):
    """Raise this Error when the convert failed"""
    pass

def convert(url):

    URL = "http://url2markdown.herokuapp.com/"
    param = {"url":url}

    res = requests.get(URL,params=param)

    if res.status_code == 200:
        return res.text

    else:
        ConvertError("convert failed")


def main():

    if len(sys.argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(1)

    parsed = parser.parse_args()

    res = convert(parsed.URL)

    if parsed.file:

        if os.access(parsed.file, os.F_OK):
            raise IOError("{} is already exist.".format(parsed.file))

        else:
            with open(parsed.file, "w") as fp:
                fp.write(res)
    else:

        print res

if __name__ == "__main__":

    main()

