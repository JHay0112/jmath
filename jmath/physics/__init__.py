'''
    jmath/physics/__init__.py

    Author: Jordan Hay
    Date: 2021-06-17

    Initialises jmath.physics
'''

# Define related components
__all__ = [
    "mechanics",
    "circuits"
]

# Import core components
from .mechanics import *
from .circuits import *