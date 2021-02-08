import os
from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='package_test',
    author='Marcus',
    description='Python package test',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/marcusboyle/package_test",
    packages=find_packages(),
    python_requires='>=3.7',
    zip_safe=False
)
