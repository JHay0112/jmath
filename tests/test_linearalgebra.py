"""
    jmath/tests/test_linearalgebra.py

    Runs tests on linear algebra component using pytest

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Imports

from ..jmath.linearalgebra import *

# - Functions

def test_vector_arithmetic():
    """Tests vector addition and subtraction"""
    # Add/Subtract
    added = Vector(1, 2) + Vector(3, 4)
    subtracted = Vector(1, 2) - Vector(3, 4)
    # Test Add
    excepted = Vector(4, 6)
    assert added.components == excepted.components
    # Test Subtract
    excepted = Vector(-2, -2)
    assert subtracted.components == excepted.components

def test_vector_scaling():
    """Tests vector multiplication and division"""
    # Divide/multiply
    multiplied = Vector(3, 4) * 4
    divided = Vector(1, 2) / 2
    # Test multiply
    expected = Vector(12, 16)
    assert multiplied.components == expected.components
    # Test divide
    expected = Vector(1/2, 1)
    assert divided.components == expected.components

def test_dot_product():
    """Tests the dot product"""
    dot = Vector(1, 2) @ Vector(3, 4)
    expected = 1*3 + 2*4
    assert dot == expected

def test_projection():
    """Tests projecting vectors"""
    # Test with vector
    vec1 = Vector(3, 4)
    vec2 = Vector(1, 1)
    expected = Vector(7/2, 7/2)
    assert vec1.projection(vec2).components == expected.components
    # Test with line
    line = Line(None, vec2)
    assert vec1.projection(line).components == expected.components

def test_magnitude():
    """Tests vector magnitude"""
    vector = Vector(3, 4, 5, -2)
    assert round(vector.magnitude(), 2) == 7.35

def test_vector_size():
    """Tests that a vector will return the correct size"""
    # Vector with six entries
    vector = Vector(1, 2, 3, 4, 5, 6)
    assert len(vector) == 6
    # Vector with one entry
    vector = Vector(0)
    assert len(vector) == 1

def test_point_in_line():
    """Tests whether a point is in a line"""
    # Test point that should be on line
    point = Point(3, 4)
    line = Line(None, 2 * point)
    assert point.on_line(line)
    # Test point that shouldn't be
    point = Point(8, 1)
    assert not point.on_line(line)

    # Testing in 3-space for certainty
    point = Point(1, 2, 3)
    d_vector = Vector(4, 5, 6)
    known_point_on_line = Point(9, 12, 15)
    line = Line(point, d_vector)
    assert known_point_on_line.on_line(line)

def test_angle_between():
    """Tests that angle between vectors is correct"""
    vec1 = Vector(1, 1)
    vec2 = Vector(2, 2)

    assert vec1.angle_between(vec2) == 0