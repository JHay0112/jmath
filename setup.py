'''
    setup.py

    Author: Jordan Hay
    Date: 2021-06-17
'''

from setuptools import find_packages, setup

setup(
    name = 'jmath',
    packages = find_packages(include=['jmath']),
    version = '1.1.0',
    description = "Mathematics Tools",
    author = "Jordan Hay",
    license = "MIT",
    url = "https://github.com/JHay0112/jmath",
    install_requires=["matplotlib==3.3.4"]
)