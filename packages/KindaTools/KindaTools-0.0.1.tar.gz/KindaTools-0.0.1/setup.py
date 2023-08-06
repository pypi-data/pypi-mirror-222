#!/usr/bin/env python
#-*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
	name = "KindaTools",
	version = "0.0.1",
	keywords = ("pip", "pathtool", "timetool", "kindatool"),
	description = "Kinda's public tools package",
	long_description = "Kinda's public tools package",
	license = "MIT Licence",
	url = "https://github.com/alndaly/kinda-python",
	author = "Kinda Hall",
	author_email = "1142704468@qq.com",
	packages = find_packages(),
	include_package_data = True,
	platforms = "any",
	install_requires = []
)