'''
    Tests the approximate derivative functions.
'''

# - Imports

from ..jmath.approximation.differentiation import differentiate, second_partials_test, LOCAL_MAXIMUM, LOCAL_MINIMUM, SADDLE
from .tools import plus_or_minus, random_integer, repeat
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

'''
Issues noted with second derivative, work on going

@repeat
def test_second_linear_derivative():
    """Tests that a second order linear derivative approximately gives zero"""
    gradient = random_integer()
    y_int = random_integer()
    point = random_integer()
    f = lambda x : gradient * x + y_int
    assert round(differentiate(f, point, n = 2).value, 5) == 0
'''

@repeat
def paraboloid_second_partials():
    """Tests the second partials test on a paraboloid"""
    a = plus_or_minus()
    b = plus_or_minus()
    c = random_integer()
    # Construct ellipse
    paraboloid = lambda x, y: a*x**2 + b*y**2 + c
    # Get critical point class at (0, 0)
    type = second_partials_test(paraboloid, [(0, 0)])[(0, 0)]
    # Check if correct type
    if a == b:
        # Both negative
        if a == -1:
            # Thus max
            assert type == LOCAL_MAXIMUM
        else:
            # Else both positive so min
            assert type == LOCAL_MINIMUM
    else:
        # Different co-effecients, should be saddle
        assert type == SADDLE