#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

version = "0.2"

setup(
    name = "dj-cmd",
    version = version,
    description = "`dj cmd` is a Django shortcut command.",
    license = "BSD",

    author = "Filip Wasilewski",
    author_email = "en@ig.ma",

    url = "https://github.com/nigma/dj-cmd",
    download_url = "https://github.com/nigma/dj-cmd/zipball/master",

    long_description = open("README.rst").read(),

    packages = ["dj_cmd"],
    package_dir = {"dj_cmd": "src"},
    include_package_data = True,
    classifiers = (
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ),
    tests_require = ["django>=1.3"],
    entry_points = {
        "console_scripts": [
            "dj = dj_cmd.dj:main",
        ]
    },
)
