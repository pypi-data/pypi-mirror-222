# coding=utf-8
"""
.. moduleauthor:: Torbjörn Klatt <t.klatt@fz-juelich.de>
"""

import importlib
import inspect
import os


def get_modules_in_path(base_package):
    """
    Finds all modules in given base package and its subpackages
    Args:
        base_package (str):
            base package to walk through
    Returns:
        list of str: list of `package.module` strings ready to be used by `import`
    """
    assert os.path.isdir(base_package), "Base package not found: %s" % base_package
    modules = []

    for root, _dirs, files in os.walk(base_package):
        package = root.replace('/', '.')
        for f in files:
            if f.endswith('.py'):
                if f == '__init__.py':
                    continue
                modules.append(package + '.' + f.replace('.py', ''))

    return modules


def load_modules_from_base(base_package):
    """
    Loads all modules of given package and its subpackages
    The list of modules and subpackages is generated by :meth:`get_modules_in_path`.
    Args:
        base_package (str):
            base package to walk through
    Returns:
        dict of modules: dict of loaded modules mapped to the `package.module` string
    """
    modules = get_modules_in_path(base_package)
    imported = {}

    for m in modules:
        print("Loading module: %s" % m)
        imported.update({m: importlib.import_module(m)})

    return imported


def get_derived_from_in_package(base_class, base_package):
    """
    Finds all derived classes of given base class in given package
    Uses :meth:`get_modules_in_path` to find all modules in given package and its subpackages,
    then loads them with :meth:`load_modules_from_base` and tests all contained classes, whether
    they are derived from `base_class`.
    Args:
        base_class (class):
            base class as class object
        base_package (str):
            as used by :meth:`get_modules_in_path`
    Returns:
        list of class objects:
            all classes in `base_package` with `base_class` in their `__mro__`
    """
    imported = load_modules_from_base(base_package)
    derived = []

    for module, loaded in imported.items():
        print("checking module '%s': %s -> %s" % (module, loaded, loaded.__dict__.keys()))
        for obj in dir(loaded):
            cls = getattr(loaded, obj)

            if not inspect.isclass(cls):
                continue

            if base_class in cls.__mro__ and cls is not base_class:
                derived.append(cls)

    return derived
