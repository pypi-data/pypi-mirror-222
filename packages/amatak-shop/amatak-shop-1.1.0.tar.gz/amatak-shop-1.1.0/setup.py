from setuptools import setup, find_namespace_packages

PACKAGES = find_namespace_packages(exclude=["amatak_shop", "eCommerce", "static_in_env"])

setup(packages=PACKAGES)