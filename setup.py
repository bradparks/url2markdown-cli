#!/usr/bin/env python
#coding: utf-8

from setuptools import setup
from url2markdown.__main__ import __version__

if __name__ == "__main__":

    setup(
        name="url2markdown-cli",
        version=__version__,
        description="Convert website to markdown from an url. Powered by http://url2markdown.herokuapp.com/",
        author="Hayato Tominaga",
        author_email="takemehighermore@gmail.com",
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
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ]
    )
