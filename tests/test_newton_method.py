"""
    Tests that Newton's Method behaves as expected.
"""

# - Imports

from ..jmath.approximation.newton_method import *

# - Tests

def test_root_2():
    """Tests that root 2 comes from the Newton Method as expected."""
    f = lambda x : x**2 - 2
    f_prime = lambda x : 2*x
    assert round(newton_method(f, f_prime, 1).value, 6) == 1.414214

def test_x_squared():
    """Tests that the root of x squared is 0 as expected."""
    f = lambda x : x**2
    f_prime = lambda x : 2*x
    assert round(newton_method(f, f_prime, 1).value, 3) == 0

def test_newton_sqrt():
    """Tests that the Newton Sqrt works."""
    assert round(newton_sqrt(2).value, 6) == 1.414214