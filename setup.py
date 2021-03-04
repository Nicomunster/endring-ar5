# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:53:02 2021

@author: nicol
"""

from distutils.core import setup
from setuptools import find_packages

requires = [
    'six>=1.10.0',
]

if __name__ == "__main__":
    setup(
        name="endring",
        version="0.0.1",
        packages=find_packages(),
        install_requires=requires,
        description='ar5 endringsdeteksjon',
        include_package_data=True,
    )