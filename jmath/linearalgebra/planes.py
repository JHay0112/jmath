'''
    Plane defined by vectors and point.
'''

# - Imports

from . import Point, Vector
from ..exceptions import VectorsNotSameSize

class Plane:
    """
        Defines a plane 

        Parameters
        ----------

        point
            Point on the plane.
        vector1
            Direction vector.
        vector2
            Direction vector.

        Raises
        ------

        VectorsNotSameSize
            If the vectors are not the same size this error will be raised.
    """
    def __init__(self, point: Point, vector1: Vector, vector2: Vector):
        
        self.point = point
        self.vectors = [vector1, vector2]

        # Throw error if vectors different sizes
        if len(point) != len(vector1) != len(vector2):
            raise VectorsNotSameSize()