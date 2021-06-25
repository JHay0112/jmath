"""
    jmath/tests/test_linearalgebra.py

    Runs tests on linear algebra component

    Author: Jordan Hay
    Date: 2021-06-25
"""

from ..linearalgebra import *

def test_vector_addition():
    added = Vector(1, 2) + Vector(3, 4)
    excepted = Vector(4, 6)
    assert added == excepted