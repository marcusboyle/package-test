import os
from setuptools import setup, find_packages


# Use README.md for long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Requirements
with open('requirements.in', 'r') as f:
    reqs = f.read().splitlines()

setup(
    name='my_package',
    author='Marcus',
    description='Python package test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/marcusboyle/package_test',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=reqs,
    zip_safe=False
)
