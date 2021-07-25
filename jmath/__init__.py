'''
    jmath/__init__.py

    The jmath top level package.

    By default includes uncertainties and linearalgebra modules.
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .uncertainties import Uncertainty
from .linearalgebra import Vector, Line