"""
    jmath/tests/test_linearalgebra.py

    Runs tests on linear algebra component using pytest

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Imports

from ..uncertainties import *
import math

# - Functions

def test_addition():
    """Tests uncertainty addition"""
    added = Uncertainty(2, 1) + Uncertainty(5, 2)
    expected = Uncertainty(7, 3)
    assert added.value == expected.value
    assert added.abs_uncertainty() == expected.abs_uncertainty()

def test_subtraction():
    """Tests uncertainty subtraction"""
    subtracted = Uncertainty(3, 1) - Uncertainty(20, 3)
    expected = Uncertainty(-17, 4)
    assert subtracted.value == expected.value
    assert subtracted.abs_uncertainty() == expected.abs_uncertainty()

def test_multiplication():
    """Tests uncertainty multiplication"""
    multiplied = Uncertainty(10, 1) * Uncertainty(3, 1)
    expected = Uncertainty(30, 13)
    assert multiplied.value == expected.value
    assert multiplied.abs_uncertainty() == expected.abs_uncertainty()

def test_division():
    """Tests uncertainty division"""
    divided = Uncertainty(3, 1) / Uncertainty(3, 2)
    expected = Uncertainty(1, 1)
    assert divided.value == expected.value
    assert divided.abs_uncertainty() == expected.abs_uncertainty()

def test_function_application():
    """Tests applying a function to an uncertainty"""
    result = Uncertainty(5, 2).apply(math.sqrt)
    expected = Uncertainty(2.2, 0.4)
    assert round(result.value, 1) == expected.value
    assert round(result.abs_uncertainty(), 1) == expected.abs_uncertainty()