'''
    setup.py

    Author: Jordan Hay
    Date: 2021-06-17
'''

from setuptools import find_packages, setup

# Open readme
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'jmath',
    packages = find_packages(include=['jmath']),
    version = 'v3.0.3',
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
    install_requires=["matplotlib", "numpy"],
    python_requires=">=3.6"
)
