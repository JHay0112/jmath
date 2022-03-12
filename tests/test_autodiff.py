'''
    Tests the auto-differentiation module
'''

# - Imports

from ..jmath.autodiff import x, y, z, a, b, c
from ..jmath import sin, ln, exp
from .tools import random_integer, repeat

# - Tests

@repeat
def test_linear_derivative():
    '''Tests the derivatives of linear functions.'''
    m = random_integer(non_zero = True)
    c = random_integer()
    y = m*x + c
    assert y.d(x) == m

@repeat
def test_power_rule():
    '''Tests the power rule.'''
    n = random_integer(2, 100)
    y = x**n
    assert y.d(x)(x = 1) == n

@repeat
def test_sin_derivative():
    '''Tests derivatives of the sine function.'''
    a = random_integer(non_zero = True)
    f = random_integer(non_zero = True)
    c = random_integer()
    y = a*sin(f*x) + c
    y_x = y.d(x)
    assert y_x(x = 0) == a*f

@repeat
def test_natural_log_derivative():
    '''Tests the derivative of the natural log.'''
    a = random_integer(non_zero = True)
    y = a*ln(x)
    assert y.d(x)(x = 1) == a

@repeat
def test_exponential_chain_rule():
    '''Tests the chain rule with the natural log.'''
    a = random_integer(non_zero = True)
    b = random_integer(non_zero = True)
    y = a*exp(b * x)
    assert y.d(x)(x = 0) == a*b

def test_trivial_partial():
    '''Tests a trivial partial derivative example.'''
    f = x * y
    assert f.d(x) == y
    assert f.d(y) == x