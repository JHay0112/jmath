'''
    setup.py

    Author: Jordan Hay
    Date: 2021-06-17
'''

from setuptools import find_packages, setup

setup(
    name = 'jmath',
    packages = find_packages(include=['jmath']),
    version = 'v3.0.2',
    description = "Mathematics Tools",
    author = "Jordan Hay",
    license = "MIT",
    url = "https://github.com/JHay0112/jmath",
    install_requires=[]
)
