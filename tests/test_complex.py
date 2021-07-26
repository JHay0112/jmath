'''
    Tests the complex number component of linearalgebra.py
'''

# - Imports

from ..jmath.linearalgebra import Complex

# - Tests

def test_quadrants():
    """Tests that complex numbers are in expected quadrants."""
    q1 = Complex(2, 1)
    q2 = Complex(-2, 1)
    q3 = Complex(-2, -1)
    q4 = Complex(2, -1)
    assert q1.quadrant() == 1
    assert q2.quadrant() == 2
    assert q3.quadrant() == 3
    assert q4.quadrant() == 4

def test_argument():
    """Tests that the argument of the complex number is as expected."""
    z = Complex(-1, 1)
    # Should be 135 degrees or 2.356 rad
    assert round(z.argument(), 3) == 2.356