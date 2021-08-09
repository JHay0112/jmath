'''
    setup.py

    Author: Jordan Hay
    Date: 2021-06-17
'''

from setuptools import setup, find_packages

# Open readme
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# Open version
with open("version.txt", "r", encoding="utf-8") as fh:
    version = fh.readline()

setup(
    name = 'jmath',
    packages = find_packages(include = [
        "jmath",
        "jmath.*"
    ]),
    version = version,
    description = "Mathematics Tools",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "Jordan Hay",
    license = "MIT",
    url = "https://github.com/JHay0112/jmath",
    project_urls={
        "Bug Tracker": "https://github.com/JHay0112/jmath/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6"
)
