import os
from setuptools import setup, find_packages

#pwd = os.path.abspath(os.path.dirname(__file__))

# with open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Needed for dependencies
# pip install --user --upgrade setuptools wheel

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
