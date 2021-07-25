"""
    jmath/exceptions.py

    Defines exceptions for jmath.
"""

# - Classes

class VectorsNotSameSize(Exception):
    """Exception throw for operations on vectors of different sizes"""
    def __init__(self, message = "Operation invalid for vectors of different sizes."):
        self.message = message
        super().__init__(self.message)

class ZeroDistance(Exception):
    """Exception thrown for calculations with zero distance between objects."""
    def __init__(self, message = "Invalid operation! Zero distance between objects."):
        self.message = message
        super().__init__(self.message)

class InvalidFractionOperation(Exception):
    """Exception thrown for invalid operations on fractions"""
    def __init__(self, message = "This operation cannot be completed on fractions."):
        self.message = message
        super().__init__(self.message)