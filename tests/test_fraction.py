"""
    jmath/tests/test_fraction.py

    Runs tests on fraction using pytest

    Author: Jordan Hay
    Date: 2021-07-01
"""

# - Imports

from ..jmath.exceptions import InvalidFractionOperation
from ..jmath.fraction import *

# - Functions

def test_flip():
    """Test fraction flipping"""
    frac = Fraction(8, 20)
    result = frac.flip()
    assert result.numerator == frac.denominator
    assert result.denominator == frac.numerator

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
    assert expected == result

def test_invalid_mul():
    """Tests invalid multiplication"""
    try:
        Fraction(1, 2) * 0.5
    except InvalidFractionOperation:
        # Throws invalid fraction operation error thus true
        assert True
    else:
        # Did not throw error, uh oh, test failed
        assert False

def test_frac_add():
    """Tests adding fractions"""
    frac1 = Fraction(2, 3)
    frac2 = Fraction(3, 5)
    result = frac1 + frac2
    expected = Fraction(19, 15)
    assert expected == result

def test_int_add():
    """Tests adding an integer to a fraction"""
    frac = Fraction(2, 3)
    result = frac + 2
    expected = Fraction(8, 3)
    assert expected == result

def test_frac_div():
    """Tests dividing fractions"""
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 2)
    result = frac1 / frac2
    expected = Fraction(4, 3)
    assert expected == result

def test_frac_simplification():
    """Tests fraction simplification"""
    frac = Fraction(2, 4)
    expected = Fraction(1, 2)
    assert frac == expected