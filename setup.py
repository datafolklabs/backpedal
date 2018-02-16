
from setuptools import setup, find_packages

LONG="""
It's like `os.walk`, but backwards... and on a bicycle.

## Core Features

- Walk directories up, down, or both directions
- Search for files, directories, or both item types
- Return first item found immediately, or list of all matching items
- 100% Test Coverage (pytest)
- 100% PEP8 Compliant (pep8, autopep8)

## Motivation?

The primary use case for Backpedal is finding files from within your current directory, and/or parent(s).  For example, both Vagrant and Fabric support running from nested sub-directories within a project while loading their associated `Vagrantfile` or `fabfile.py` from the root (parent) project directory by searching from the current directory and upward.
"""

setup(name='backpedal',
    version='0.9.10',
    description="Backpedal",
    long_description=LONG,
    author='BJ Dierkes',
    author_email='derks@datafolklabs.com',
    url='http://github.com/datafolklabs/backpedal',
    license='BSD-three-clause',
    packages=find_packages(exclude=['ez_setup', 'example', 'tests']),
    include_package_data=True,
    zip_safe=False,
)
