'''
    Test Universal Trigonometric Functions
'''

# - Imports

from .tools import repeat, random_integer
from ..jmath.universal.trigonometry import sin, asin, cos, acos, tan, atan
from ..jmath.uncertainties import Uncertainty
from ..jmath.units import Unit, other
import math

# - Tests

@repeat
def test_sin():
    """Tests the sin trigonometric function."""
    a = random_integer()
    b = random_integer()
    # Normal numbers
    assert sin(a) == math.sin(a)
    assert asin(a / 100) == math.asin(a / 100)
    # Uncertainties
    #c = Uncertainty(a, b)
    #jmath_c = sin(c)
    #math_c = Uncertainty(math.sin(c.value), math.sin(c.value + c.abs_uncertainty()))
    #assert math_c == jmath_c