'''
    Standard maths functions that are also compatible with jmath structures.
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .trigonometry import sin, asin, cos, acos, tan, atan
from .logarithms import log, log10, log2, ln
from .natural import exp
from .hyperbolic import sinh, asinh, cosh, acosh, tanh, atanh