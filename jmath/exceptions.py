"""
    jmath/exceptions.py

    Defines jmath exceptions

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Classes

class VectorsNotSameSize(Exception):
    """Exception thrown for operations on vectors of different sizes."""
    def __init__(self, message = "Invalid operation! Vectors different sizes."):
        self.message = message
        super().__init__(self.message)

class ZeroDistance(Exception):
    """Exception thrown for calculations with zero distance between objects."""
    def __init__(self, message = "Invalid operation! Zero distance between objects."):
        self.message = message
        super().__init__(self.message)