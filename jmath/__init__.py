'''
    jmath/__init__.py

    Author: Jordan Hay
    Date: 2021-07-23

    Initialises folder as module
'''

# - Namespace
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .uncertainties import Uncertainty
from .linearalgebra import Vector, Line