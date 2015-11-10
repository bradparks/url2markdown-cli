#!/usr/bin/env python
#coding: utf-8

from setuptools import setup

__original__     = "https://github.com/kennethreitz/url2markdown"
__author__       = "Hayato Tominaga"
__author_email__ = "takemehighermore@gmail.com"
__version__      = "0.1a"
__license__      = "GPLv3"

if __name__ == "__main__":

    setup(
        name="url2markdown-cli",
        version=__version__,
        description="Convert website to markdown from an url. Powered by http://url2markdown.herokuapp.com/",
        author=__author__,
        author_email=__author_email__,
        url="https://github.com/alice1017/url2markdown-cli",
        packages=["url2markdown"],
        include_package_data = True,
        entry_points={
            'console_scripts': [
                'url2markdown=url2markdown.__main__:main'
            ]
        },
        install_requires=["setuptools","requests"],
        classifiers=[
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
        ]
    )
