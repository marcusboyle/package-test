# package_test
This repo is a simple test to create a sample Python package.

Structure (note that `my_package` is the package that will be created):
- `package_test`
  - `README.md`
  - `.gitignore`
  - `requirements.txt`
  - `setup.py`
  - `my_package`
    - `__init__.py`
    - `module.py`
    - `tools`
        - `__init__.py`
        - `other_module.py`
        - `numpy_module.py`

***

As a general guide, here are the steps to create a package:
1. Create a repository, e.g. `package_test`.
2. Create a subdirectory inside this repository - this will be your package.
    - The name of this subdirectory will be the name of your package. Let's refer to it as `my_package`.
3. Inside `my_package`, add an `__init__.py` file. This will define all of the imports to conduct when importing your package.
    - All modules/functions/classes/etc. that are available to `__init__.py` will become an attribute of the package.
    - This will need to be repeated for all sub-directories inside the package (i.e., add another `__init__.py` and import all modules/attributes you want to be available here -- see the example in `my_package/tools/__init__.py`).
4. In the top level of the repository, add a file called `setup.py`. You will need to fill out a setuptools.setup() call - see the file in this repo for an example.
5. You're now ready to pip install! Simply run `pip install .` (or more generally, `pip install path/to/repo`) to install this repository as a package. This will add the package to `Lib/site-packages` in your current Python installation/interpreter. You'll now be able to import it from any directory.
