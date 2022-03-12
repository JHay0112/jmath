'''
    Tests the auto-differentiation module
'''

# - Imports

from ..jmath.autodiff import analyse, Variable, Function, x, y, z, a, b, c
from ..jmath import sin, cos, ln, exp, Uncertainty
from math import pi
from .tools import random_integer, repeat

# - Tests

@repeat
def test_linear_derivatives():
    '''Tests the derivatives of linear functions.'''
    m = random_integer(non_zero = True)
    c = random_integer()
    y = m*x + c
    assert y.d(x) == m

@repeat
def test_sin_derivative():
    '''Tests derivatives of the sine function.'''
    a = random_integer(non_zero = True)
    f = random_integer(non_zero = True)
    c = random_integer()
    y = a*sin(f*x) + c
    y_x = y.d(x)
    assert y_x(x = 0) == a*f