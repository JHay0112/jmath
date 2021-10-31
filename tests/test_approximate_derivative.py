'''
    Tests the approximate derivative functions.
'''

# - Imports

from ..jmath.approximation.differentiation import differentiate
from .tools import random_integer, repeat
from math import sin, cos, pi

# - Tests

@repeat
def test_sine_derivative():
    """Tests that the sine function approximately gives a derivative of 1 at multiples of pi."""
    assert round(differentiate(sin, random_integer() * 2 * pi).value, 5) == round(1, 5)

@repeat
def test_cosine_derivative():
    """Tests that the cosine function approximately gives a derivative of 0 at multiples of pi."""
    assert round(differentiate(cos, random_integer() * 2 * pi).value, 5) == round(0, 5)

@repeat
def test_linear_derivative():
    """Tests that a linear functions approximately gives a derivative equal to it's gradient at all points."""
    gradient = random_integer()
    y_int = random_integer()
    point = random_integer()
    f = lambda x : gradient * x + y_int
    assert round(differentiate(f, point).value, 5) == round(gradient, 5)

@repeat
def test_second_linear_derivative():
    """Tests that a second order linear derivative approximately gives zero"""
    gradient = random_integer()
    y_int = random_integer()
    point = random_integer()
    f = lambda x : gradient * x + y_int
    assert round(differentiate(f, point, n = 2).value, 5) == 0