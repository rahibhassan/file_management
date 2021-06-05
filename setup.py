# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in file_management/__init__.py
from file_management import __version__ as version

setup(
	name='file_management',
	version=version,
	description='Store and retrieve files',
	author='Raheeb',
	author_email='raheeb@tridz.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
