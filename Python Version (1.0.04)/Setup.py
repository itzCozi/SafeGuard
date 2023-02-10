# How to chcek if path exists in python
"""
import os
if not os.path.exists('my_folder'):
    return False
"""
# how to check user name in python
"""
import os

username = os.getlogin()
"""
from setuptools import setup, find_packages

setup(
	name='SafeGuard-Python',
	version='1.0.0',
	packages=find_packages(),
	url='https://itzcozi.github.io/SafeGuard/',
	license='https://itzcozi.github.io/SafeGuard/license.html',
	author='itzCozi',
	author_email='',
	description='A automated setup for SafeGuard first install python 3.10 or up'
)
