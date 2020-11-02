'''
    jmath.py

    Author: Jordan Hay
    Date: 2020-11-02
    Version: 0.0.0

    Jordan's Math Module

    Creating my own maths tools in Python as a challenge.
'''

# - Modules

import math # Mathematical functions, e.g. sqrt()

# - Classes

# -- nVector
# Author: Jordan Hay
# Date: 2020-11-02
# Version: 0.0.0
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

# - Main

# Used for testing components as I develop them
if(__name__ == "__main__"):

    v = nVector(2, 3, 10)

    print(v.get_magnitude())