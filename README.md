# package_test
This repo is a simple test to create a sample Python package.

Structure (note that `my_package` is the package that will be created):
- `package_test`
  - `README.md`
  - `.gitignore`
  - `my_package`
    - `__init__.py`
    - `module.py`

***

As a general guide, here are the steps to create a package:
1. Create a repository, e.g. `package_test`.
2. Create a subdirectory inside this repository - this will be your package.
    - The name of this subdirectory will be the name of your package. Let's refer to it as `my_package`.
3. Inside `my_package`, add an `__init__.py` file. This will define all of the imports to conduct when importing your package.
    - All modules/functions/classes/etc. that are available to `__init__.py` will become an attribute of the package.
    - For example:
        - Let's say we have a module inside `my_package` called `module.py`, which contains a function called `hello_world()`.
        - If `__init__.py` contains the statement `from my_package import module` then we can access `hello_world()` through `my_package.functions.hello_world()`.
        - If `__init__.py` contains the statement `from my_package import module` then we can access `hello_world()` through `my_package.hello_world()`.
4. In the top level of the repository, at