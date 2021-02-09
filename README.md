# package_test
This repo is a simple test to create a sample Python package.

***
## Repo structure

Below is the structure of this repository. Note that `my_package` is the package that will be created.
- `package_test`
  - `README.md`
  - `.gitignore`
  - `create_venv.sh`
  - `requirements.in`
  - `setup.py`
  - `my_package`
    - `__init__.py`
    - `module.py`
    - `tools`
        - `__init__.py`
        - `other_module.py`
        - `numpy_module.py`

***
## Overview

As a general guide, here are the steps to create a package:
1. Create a repository, e.g. `package_test`.
2. Create a subdirectory inside this repository - this will be your package.
    - The name of this subdirectory will be the name of your package. Let's refer to it as `my_package`.
3. Inside `my_package`, add an `__init__.py` file. This will define all of the imports to conduct when importing your package.
    - All modules/functions/classes/etc. that are available to `__init__.py` will become an attribute of the package.
    - This will need to be repeated for all sub-directories inside the package (i.e., add another `__init__.py` and import all modules/attributes you want to be available here -- see the example in `my_package/tools/__init__.py`).
4. In the top level of the repository, add a file called `setup.py`. You will need to fill out a setuptools.setup() call - see the file in this repo for an example.
    - Note that, if you want your package to automatically install dependencies, you will need to create a requirements file containing all dependencies that need to be installed (see `requirements.in` for an example). These can then be passed in (as a list of strings for each package) to the `install_requires` parameter in `setup()`.
5. You're now ready to pip install!

***
## Pip installing the package
### Installing from a local repository

If you have this repository available locally (e.g. you've cloned it), then while inside `package_test`, simply run `pip install .` (or more generally, `pip install path/to/repo`) to install this repository as a package. This will add the package to `Lib/site-packages` in your current Python installation/interpreter. You'll now be able to import it from any directory.

### Installing this package from GitHub remote

Rather than cloning the repository to have a local copy, you can directly install this package with only one line of code (no need to clone etc.). Simply run the following:
```
pip install git+git://github.com/marcusboyle/package_test.git
```
