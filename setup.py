#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Get the version
import re
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('hyper/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        version = match.group(1)
    else:
        raise RuntimeError("No version number found!")

# Stealing this from Kenneth Reitz
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['hyper']

setup(
    name='hyper',
    version=version,
    description='HTTP/2.0 for Python',
    long_description=open('README.rst').read(),
    author='Cory Benfield',
    author_email='cory@lukasa.co.uk',
    url='',
    packages=packages,
    package_data={'': ['LICENSE', 'README.rst', 'CONTRIBUTORS.rst']},
    package_dir={'hyper': 'hyper'},
    include_package_data=True,
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    )
)
