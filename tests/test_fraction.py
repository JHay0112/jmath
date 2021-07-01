"""
    jmath/tests/test_fraction.py

    Runs tests on fraction using pytest

    Author: Jordan Hay
    Date: 2021-07-01
"""

# - Imports

from ..jmath.fraction import *

# - Functions

def test_flip():
    """Test fraction flipping"""
    frac = Fraction(8, 20)
    frac.flip()
    assert frac.numerator == 20
    assert frac.denominator == 8

def test_frac_mul():
    """Tests multiplying fractions together"""
    frac1 = Fraction(7, 3)
    frac2 = Fraction(2, 3)
    expected_frac = Fraction(14, 9)
    result_frac = frac1 * frac2
    assert expected_frac.numerator == result_frac.numerator
    assert expected_frac.denominator == result_frac.denominator

def test_int_mul():
    """Tests scaling a fraction with an int"""
    frac = Fraction(3, 8)
    scaler = 5
    expected = Fraction(15, 8)
    result = scaler * frac
    assert expected.numerator == result.numerator
    assert expected.denominator == result.denominator