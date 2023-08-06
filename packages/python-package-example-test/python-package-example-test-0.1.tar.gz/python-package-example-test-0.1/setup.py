
from setuptools import setup, find_packages

setup(
    name='python-package-example-test',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    description='An example python package',
)
