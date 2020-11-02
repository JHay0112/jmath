'''
    jmath.py

    Author: Jordan Hay
    Date: 2020-11-02
    Version: 0.4.1

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
# Version: 0.4.1
# A vector with n dimensions
class nVector:

    # --- __init__()
    # Initialise nVector object
    #
    # self
    # *components (List/*args) - Scalar vector components, e.g. x, y, z
    def __init__(self, *components):

        # If components[0] is list store that list
        if(type(components[0]) == list):
            self._components = components[0]
        else:
            # Else it's *args
            self._components = components

    # --- __add__()
    # Add another nVector object to this nVector
    #
    # self
    # vector (nVector) - The foreign nVector to add
    def __add__(self, vector):

        # Add the foreign components to local components and return
        return(nVector(list(map(operator.add, self._components, vector.get_components()))))

    # --- __sub__()
    # Subtract another nVector object from this vector
    #
    # self
    # vector (nVector) - The foreign nVector to subtract
    def __sub__(self, vector):

        # Subtract the foreign components from local components and return
        return(nVector(list(map(operator.sub, self._components, vector.get_components()))))

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

# - Main

# Used for testing components as I develop them
if(__name__ == "__main__"):

    v = nVector(2, 3, 10)
    fv = nVector(1, 2, 3)

    v += fv
    v -= fv

    print(v.get_components())