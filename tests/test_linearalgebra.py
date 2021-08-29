"""
    jmath/tests/test_linearalgebra.py

    Runs tests on linear algebra component using pytest

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Imports

from ..jmath.linearalgebra import Vector, Point, Line
from .tools import random_integer, random_integers, repeat
from typing import Tuple, List
from math import sqrt

# - Functions

def vector_component_pair(len: int = random_integer()) -> Tuple[Vector, List[int]]:
    """
        Generates a vector and component pair randomly.
        
        Parameters
        ----------

        len
            The length vector/components to generate
    """
    components = random_integers(len)
    return (Vector(components), components)

@repeat
def test_vector_equality():
    """Tests that vectors are equal as expected."""
    v, c = vector_component_pair()

    assert v == v
    assert v == Vector(c)
    assert v.components == c

@repeat
def test_vector_addition():
    """Tests vector addition."""
    len = random_integer()
    v1, c1 = vector_component_pair(len)
    v2, c2 = vector_component_pair(len)

    expected = Vector([i + j for i, j in zip(c1, c2)])

    assert (v1 + v2) == expected

@repeat
def test_vector_subtraction():
    """Tests vector subtraction."""
    len = random_integer()
    v1, c1 = vector_component_pair(len)
    v2, c2 = vector_component_pair(len)

    expected = Vector([i - j for i, j in zip(c1, c2)])

    assert (v1 - v2) == expected

@repeat
def test_vector_scaling():
    """Tests vector multiplication and division"""
    # Produce initial conditions
    length = random_integer(min = 3, max = 10)
    scalor = random_integer(min = 1, max = 10)
    v, c = vector_component_pair(length)

    # Mult/div vectors
    mult = v * scalor
    div = v / scalor

    # Compute expected
    mult_expected = Vector([scalor * i for i in c])
    div_expected = Vector([round(i / scalor, 5) for i in c])

    # Round division vector to factor out floating point error
    div.components = [round(i, 5) for i in div.components]

    # Test multiply
    assert mult_expected == mult
    # Test divide
    assert div_expected == div

@repeat
def test_dot_product():
    """Tests the dot product"""
    # Generate vectors and components
    len = random_integer()
    v1, c1 = vector_component_pair(len)
    v2, c2 = vector_component_pair(len)

    # Compute dot product
    dot = v1 @ v2

    # Predict dot product
    predicted_dot = sum([i * j for i, j in zip(c1, c2)])

    assert dot == predicted_dot

def test_projection():
    """Tests projecting vectors"""
    # Test with vector
    vec1 = Vector(3, 4)
    vec2 = Vector(1, 1)
    expected = Vector(7/2, 7/2)
    assert vec1.projection(vec2) == expected
    # Test with line
    line = Line(Point(0, 0), vec2)
    assert vec1.projection(line) == expected

@repeat
def test_magnitude():
    """Tests vector magnitude"""
    
    v, c = vector_component_pair()

    # Square components, sum, and sqrt
    predicted_magnitude = sqrt(sum([i ** 2 for i in c]))

    assert round(predicted_magnitude, 5) == round(v.magnitude(), 5)

@repeat
def test_vector_size():
    """Tests that a vector will return the correct size"""
    
    v, c = vector_component_pair()

    assert len(v) == len(c)

def test_point_in_line():
    """Tests whether a point is in a line"""
    # Test point that should be on line
    point = Point(3, 4)
    line = Line(Point(0, 0), 2 * point)
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

@repeat
def test_negative():
    """Test that a negative vector does indeed give one with all the components reversed"""

    # Generate vector component pair
    v, c = vector_component_pair()
    # Make negative vector
    v = v.negative()
    # Make components negative
    c = Vector([-i for i in c])
    
    assert v == c

def test_unit_vector():
    """Tests that a unit vector is produced correctly"""
    vec = Vector(1, 2)
    unit_vec = vec.unit()
    assert round(unit_vec.magnitude(), 10) == 1
    assert vec.magnitude() * unit_vec == vec