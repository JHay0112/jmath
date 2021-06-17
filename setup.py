'''
    setup.py

    Author: Jordan Hay
    Date: 2021-06-17
'''

from distutils.core import setup

setup(
    name = 'jmath',
    packages = ['jmath'],
    version = '1.0.1',
    description = "Mathematics Tools",
    author = "Jordan Hay",
    license = "MIT",
    url = "https://github.com/JHay0112/jmath",
    install_requires=["matplotlib==3.3.4"]
)