'''
    Linear algebra objects including Vectors, Points, Lines, and Planes.
'''

# - Components

from .exceptions import VectorsNotSameSize

# - Modules

import math # Mathematical functions, e.g. sqrt()
from typing import List, Union, Callable, Any
from functools import wraps

# - Classes
class Vector:
    """
        n-dimensional Vectors

        Parameters
        ----------

        components
            Scalar vector components

        Examples
        --------

        >>> Vector(3, 2, 1) + Vector(2, 1, 1)
        Vector(5, 3, 2)

        >>> Vector(3, 1, 0) - Vector(9, 8, 8)
        Vector(-6, -7, -8)

        >>> 3 * Vector(1, 2, -4)
        Vector(3, 6, -12)
        >>> Vector(3, 6, 9)/3
        Vector(1, 2, 3)

        >>> Vector(10, 2, 1) @ Vector(1, 2, 3)
        17

        >>> Vector(1, 1).magnitude()
        2

    """
    def __init__(self, *components: List[float]):

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self.components = components[0]
        else:
            # Else it's *args
            self.components = list(components)

    def __repr__(self) -> str:
        """Programming Representation"""
        return f"Vector{self.__str__()}"

    def __str__(self) -> str:
        """String representation"""
        string = "("
        for component in self.components:
            string += f"{component}, "
        string = string[:-2] + ")"
        return string

    def __same_size(func: Callable[["Vector", "Vector"], Any]) -> Callable[["Vector", "Vector"], Any]:
        """
            Wrapper that checks if vectors are the same size.

            Parameters
            ----------

            func
                Function to check

            Raises
            ------

            VectorsNotSameSize
                If the vectors are not the same size this error will be raised.
        """
        @wraps(func)
        def inner(*args, **kwargs):
            if len(args[0]) == len(args[1]):
                return func(*args, **kwargs)
            else:
                raise VectorsNotSameSize()

        return inner

    def __eq__(self, vector: "Vector") -> bool:
        """Tests equality of vectors"""
        if isinstance(vector, Vector) or isinstance(vector, Point):
            return vector.components == self.components
        else:
            return False

    @__same_size
    def __add__(self, vector: "Vector") -> "Vector":
        """Add vectors together"""

        # Add the foreign components to local components and return
        return Vector([i + j for i, j in zip(self.components, vector.components)])

    @__same_size
    def __sub__(self, vector: "Vector") -> "Vector":
        """Subtract vectors from each other"""
        
        # Subtract the foreign components from local components and return
        return Vector([i - j for i, j in zip(self.components, vector.components)])

    @__same_size
    def __matmul__(self, vector: "Vector") -> float:
        """The dot product of two vectors"""
        return sum([i * j for i, j in zip(self.components, vector.components)])

    def __mul__(self, scalar: float) -> "Vector":
        """Scalar multiplication"""

        new_components = [scalar * component for component in self.components]
        return Vector(new_components)

    def __rmul__(self, scalar: float) -> "Vector":
        """Reverse scalar multiplication"""
        return self * scalar

    def __truediv__(self, scalar: float) -> "Vector":
        """Scalar division"""
        return 1/scalar * self

    def __rtruediv__(self, scalar: float) -> "Vector":
        """Reverse scalar division"""
        return self * 1/scalar

    def __len__(self) -> int:
        """Amount of components in vector"""
        return len(self.components)

    def unit(self) -> "Vector":
        """Returns a unit vector in the same direction as the vector."""
        return self/self.magnitude()

    def negative(self) -> "Vector":
        """Returns a vector of the same magnitude pointing in the opposite direction."""
        neg_comp = [-component for component in self.components]
        return Vector(neg_comp)

    @__same_size
    def projection(self, vector: Union["Vector", "Line"]) -> "Vector":
        """
            Returns projection of current vector onto the passed vector or line.

            Parameters
            ----------

            vector
                Vector or line to calculate the projection onto.

            Raises
            ------

            VectorsNotSameSize
                If the vectors are not the same size this error will be raised.
        """
        if isinstance(vector, Line):
            vector = vector.vector

        return (self @ vector)/(vector @ vector) * vector

    def magnitude(self) -> float:
        """Calculates the vector magnitude."""
        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self.components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    @__same_size
    def angle_between(self, vector: "Vector") -> float:
        """
            Determines the angle (in radians) between two vectors to 5 d.p.

            Parameters
            ----------

            vector
                Vector or line to calculate angle between.

            Raises
            ------

            VectorsNotSameSize
                If the vectors are not the same size this error will be raised.
        """

        if isinstance(vector, Line):
            vector = vector.vector

        return round(math.acos((self @ vector)/(self.magnitude() * vector.magnitude())), 5)

class Complex(Vector):
    """
        Complex numbers based on vectors.

        Parameters
        ----------

        real
            Real component of a complex number
        imaginary
            Imaginary component of a complex number
    """

    def __init__(self, real: float, imaginary: float):
        
        super().__init__(real, imaginary)

    def __repr__(self) -> str:
        """Programming Representation"""
        return f"ComplexNumber({self.real}, {self.imaginary})"

    def __str__(self) -> str:
        """String representation"""
        operand = ""
        if self.imaginary >= 0:
            operand = "+"
        return f"{self.real()} {self.operand} {self.imaginary()}j"

    def real(self):
        """Returns the real component of the complex number."""
        return self.components[0]

    def imaginary(self):
        """Returns the imaginary component of the complex number."""
        return self.components[1]

    def quadrant(self) -> Union[int, None]:
        """Returns which quadrant the number is in. Returns None if on a quadrant border."""
        if self.real() > 0 and self.imaginary() > 0:
            # Both greater than zero
            # Quadrant 2
            return 1
        elif self.real() < 0 and self.imaginary() > 0:
            # Real is less than zero and imaginary greater than
            # Quadrant 2
            return 2
        elif self.real() < 0 and self.imaginary() < 0:
            # Real and imaginary less than zero
            # Quadrant 3
            return 3
        elif self.real() > 0 and self.imaginary() < 0:
            # Real greater than zero but imaginary negative
            # Quadrant 4
            return 4
        else:
            # On a border
            return None

    def argument(self) -> float:
        """Computes the argument of the complex number in radians."""
        theta = math.atan(self.imaginary()/self.real())
        # Check quadrant
        if self.quadrant() == 2:
            # If in the second quadrant
            # Add pi
            theta += math.pi
        elif self.quadrant() == 3:
            # If in third quadrant
            # Subtract pi
            theta -= math.pi

        return theta

    def modulus(self) -> float:
        """Rename of magnitude."""
        return self.magnitude()

class Point(Vector):
    """
        Points based on vector framework. Can be thought of as a vector from origin.

        Parameters
        ----------

        components
            Coordinates in n-space
    """
    def __init__(self, *components: List[float]):
        return super().__init__(*components)
    
    def on_line(self, line: "Line") -> bool:
        """
            Determines whether a point is on a line, returns bool.

            Parameters
            ----------

            line
                Line to determine if on
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
        Defines a line from direction and point vectors.

        Parameters
        ----------

        point
            Position vector for line.
        vector
            Direction vector for line.
    """
    def __init__(self, point: Point, vector: Vector):
        self.point = point
        self.vector = vector

        if self.point == None:
            self.point = Point([0 for i in self.vector.components])

        if len(self.point) != len(self.vector):
            raise VectorsNotSameSize()

    def __len__(self) -> int:
        """Returns size of direction vector"""
        return len(self.vector.components)

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