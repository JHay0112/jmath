'''
    jmath/linearalgebra.py

    Author: Jordan Hay
    Date: 2021-06-17

    Vectors
'''

# - Components

from . import exceptions

# - Modules

import operator # Python operators
import math # Mathematical functions, e.g. sqrt()
from typing import List, Union, Callable, Any

# - Classes
class Vector:
    """
        n-dimensional Vectors

        Arguments:

        \*components (floats) - Scalar vector components

        Author: Jordan Hay
        Date: 2020-11-02
    """
    def __init__(self, *components: List[float]):

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self.components = components[0]
        else:
            # Else it's *args
            self.components = list(components)

    def __str__(self) -> str:
        """String representation"""
        string = "("
        for component in self.components:
            string += f"{component}, "
        string = string[:-2] + ")"
        return string

    def same_size(func: Callable[["Vector", "Vector"], Any]) -> Callable[["Vector", "Vector"], Any]:
        """
            Wrapper that checks if vectors are the same size

            Parameters:

            func (function) - Function to check
        """

        def inner(*args, **kwargs):
            if len(args[0]) == len(args[1]):
                return func(*args, **kwargs)
            else:
                raise exceptions.VectorsNotSameSize()

        return inner

    def __eq__(self, vector: "Vector") -> bool:
        """Tests equality of vectors"""
        if isinstance(vector, Vector) or isinstance(vector, Point):
            return vector.components == self.components
        else:
            return False

    @same_size
    def __add__(self, vector: "Vector") -> "Vector":
        """
            Add vectors together

            Parameters

            vector (Vector) - Vector to add
        """

        # Add the foreign components to local components and return
        return(Vector(list(map(operator.add, self.components, vector.components))))

    @same_size
    def __sub__(self, vector: "Vector") -> "Vector":
        """
            Subtract vectors from each other

            Parameters:

            vector (Vector) - Vector to subtract
        """
        # Subtract the foreign components from local components and return
        return(Vector(list(map(operator.sub, self.components, vector.components))))

    @same_size
    def __matmul__(self, vector: "Vector") -> float:
        """
            The dot product of two vectors

            Parameters:

            vector (Vector) - Vector to dot with
        """
        dot = 0
        for i in range(len(self.components)):
            dot += self.components[i] * vector.components[i]
        return dot

    def __mul__(self, scalar: float) -> "Vector":
        """
            Scalar multiplication

            Parameters:

            scalar (float) - Scalar amount to multiply by
        """

        new_components = [scalar * component for component in self.components]
        return Vector(new_components)

    def __rmul__(self, scalar: float) -> "Vector":
        """Reverse scalar multiplication"""
        return self * scalar

    def __truediv__(self, scalar: float) -> "Vector":
        """
            Scalar division

            Parameters:

            scalar (float) - Scalar amount to divide by
        """
        return 1/scalar * self

    def __rtruediv__(self, scalar: float) -> "Vector":
        """Reverse scalar division"""
        return self * 1/scalar

    def __len__(self) -> int:
        """Amount of components in vector"""
        return len(self.components)

    def unit(self) -> "Vector":
        """Returns a unit vector in the same direction as the vector"""
        return self/self.magnitude()

    def negative(self) -> "Vector":
        """Returns the negative vector"""
        neg_comp = [-component for component in self.components]
        return Vector(neg_comp)

    @same_size
    def projection(self, vector: Union["Vector", "Line"]) -> "Vector":
        """
            Returns projection of current vector onto passed vector

            Parameters:

            vector (Vector/Line) - Vector or line to calculate the projection onto
        """
        if isinstance(vector, Line):
            vector = vector.vector

        return (self @ vector)/(vector @ vector) * vector

    def magnitude(self) -> float:
        """Calculates the vector magnitude"""
        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self.components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    @same_size
    def angle_between(self, vector: "Vector") -> float:
        """
            Determines the angle (in radians) between two vectors to 5 d.p.

            vector (Vector/Line) - Vector or line to calculate angle between
        """

        if isinstance(vector, Line):
            vector = vector.vector

        return round(math.acos((self @ vector)/(self.magnitude() * vector.magnitude())), 5)

class Point(Vector):
    """
        Points based on vector framework. Can be thought of as a vector from origin.

        Parameters:

        \*components (\*args) - Coordinates in n-space
    """
    def __init__(self, *components: List[float]):
        return super().__init__(*components)
    
    def on_line(self, line: "Line") -> bool:
        """
            Determines whether a point is on a line, returns bool

            Parameters:

            line (Line) - Line to determine if on
        """
        results = []
        # For every component in both
        for i in range(len(self)):
            scalor = (self.components[i] - line.point.components[i])/line.vector.components[i]
            results.append(round(scalor, 3))
        # Go through results, if any don't match, return false
        return all(result == results[0] for result in results)

class Line:
    """
        Defines a line from a vector

        Parameters:

        point (Point) - Position vector for line
        vector (Vector) - Direction vector for line

        Author: Jordan Hay
        Date: 2021-06-24
    """
    def __init__(self, point: Point, vector: Vector):
        self.point = point
        self.vector = vector

        if self.point == None:
            self.point = Point([0 for i in self.vector.components])

        if len(self.point) != len(self.vector):
            raise exceptions.VectorsNotSameSize()

    def __len__(self) -> int:
        """Returns size of direction vector"""
        return len(self.vector.components)

class Plane:
    """
        Defines a plane 

        Parameters:

        point (Point/Vector) - Point on the plane
        vector1 (Vector) - Direction vector
        vector 2 (Vector) - Direction vector

        Author: Jordan Hay
        Date: 2021-06-24
    """
    def __init__(self, point: Point, vector1: Vector, vector2: Vector):
        
        self.point = point
        self.vectors = [vector1, vector2]

        # Throw error if vectors different sizes
        if len(point) != len(vector1) != len(vector2):
            raise exceptions.VectorsNotSameSize()