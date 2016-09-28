#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "1.0.0"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open("README.rst").read()

setup(
    name="dj-cmd",
    version=version,
    description="`dj cmd` is a shortcut for Django's `python manage.py` commands.",
    license="BSD",
    author="Filip Wasilewski",
    author_email="en@ig.ma",
    url="https://github.com/nigma/dj-cmd",
    long_description=readme,
    packages=[
        "dj_cmd"
    ],
    package_dir={"dj_cmd": "src"},
    include_package_data=True,
    keywords="django command shortcuts",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    tests_require=["django>=1.3"],
    entry_points={
        "console_scripts": [
            "dj = dj_cmd.dj:main",
        ]
    },
)
