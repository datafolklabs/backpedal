
from setuptools import setup, find_packages

setup(name='backpeddle',
    version='0.9.1',
    description="Backpeddle",
    long_description="Backpeddle",
    author='BJ Dierkes',
    author_email='derks@datafolklabs.com',
    url='http://github.com/datafolklabs/backpeddle',
    license='None',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
)


