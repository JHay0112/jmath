'''
    jmath.py

    Author: Jordan Hay
    Date: 2020-11-02
    Version: 0.3

    Jordan's Math Module

    Creating my own maths tools in Python as a challenge.
'''

# - Modules

import math # Mathematical functions, e.g. sqrt()
import operator # Python operators

# - Classes

# -- nVector
# Author: Jordan Hay
# Date: 2020-11-02
# Version: 0.3
# 
# A vector with n dimensions
class nVector:

    # --- __init__()
    # Initialise nVector object
    #
    # self
    # *components (Int) - Scalar vector components, e.g. x, y, z
    def __init__(self, *components):

        # Store parameters
        self._components = components

    # --- get_components()
    # Returns the components of the vector
    #
    # self
    def get_components(self):

        return(self._components)

    # --- get_magnitude()
    # Returns the magnitude of the vector as calculated from the components
    #
    # self
    def get_magnitude(self):

        # Store magnitude while computing
        magnitude = 0

        # For every vector component
        for c in self._components:
            # Pythagorean theorom
            # hypotenuse = sqrt(a**2 + b**2)
            magnitude = math.sqrt(magnitude ** 2 + c ** 2)

        return(magnitude)

    # --- add()
    # Add another nVector object to this nVector
    #
    # self
    # vector (nVector) - The foreign nVector to add
    def add(self, vector):

        # Add the foreign components to local components and set local components as equal
        self._components = list(map(operator.add, self._components, vector.get_components()))

    # --- subtract()
    # Subtract another nVector object from this vector
    #
    # self
    # vector (nVector) - The foreign nVector to subtract
    def subtract(self, vector):

        # Subtract the foreign components from local components and set local components as equal
        self._components = list(map(operator.sub, self._components, vector.get_components()))

# - Main

# Used for testing components as I develop them
if(__name__ == "__main__"):

    v = nVector(2, 3, 10)
    fv = nVector(1, 2, 3)

    v.add(fv)
    v.subtract(fv)

    print(v.get_components())