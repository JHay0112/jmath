'''
    The jmath top level package. Provides a set of default and optional sub-packages for doing maths in Python.

    Testing
    -------

    Testing can be performed upon the entire jmath codebase using

        $ pytest

    when in the jmath root directory.

    Documentation
    -------------

    Upon addition of a new sub-module the documentation must be updated with

        $ sphinx-apidoc -o ./docs/source/ ./jmath --force

    when in the jmath root directory.

    Documentation is automatically built by a workflow in github and published to https://jordanhay.com/jmath
        
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .uncertainties import Uncertainty
from .linearalgebra import Vector, Point, Line
from .modular import extended_gcd, modular_inverse