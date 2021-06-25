"""
    jmath/tests/test_linearalgebra.py

    Runs tests on linear algebra component using pytest

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Imports

from ..linearalgebra import *

# - Functions

def test_vector_addition():
    """Tests vector addition"""
    added = Vector(1, 2) + Vector(3, 4)
    excepted = Vector(4, 6)
    assert added.components == excepted.components