'''
    Tests that vectors project onto planes as expected.
'''

# - Imports

from ..jmath.linearalgebra import Vector, Point, Plane

# - Tests

def test_plane_projection():
    """Tests that a vector projects onto a plane as expected."""
    # Standard plane
    plane = Plane(Point(0, 0, 0), Vector(1, 0, 0), Vector(0, 1, 0))
    # Vector hanging over the plane
    vector = Vector(1, 2, 1)
    # Projected vector
    projection = vector.projection(plane)
    
    assert projection == Vector(1, 2, 0)