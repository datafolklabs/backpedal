
from setuptools import setup, find_packages

setup(name='backpedal',
    version='0.9.1',
    description="Backpedal",
    long_description="Backpedal",
    author='BJ Dierkes',
    author_email='derks@datafolklabs.com',
    url='http://github.com/datafolklabs/backpedal',
    license='BSD-three-clause',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
)
