"""
    jmath/exceptions.py

    Defines exceptions for jmath.
"""

# - Classes

class VectorsNotSameSize(Exception):
    """Exception thrown for operations on vectors of different sizes"""
    def __init__(self, message = "Operation invalid for vectors of different sizes."):
        self.message = message
        super().__init__(self.message)

class ZeroDistance(Exception):
    """Exception thrown for calculations with zero distance between objects."""
    def __init__(self, message = "Invalid operation! Zero distance between objects."):
        self.message = message
        super().__init__(self.message)

class OutOfRange(Exception):
    """
        Exception thrown for values that are not within expected bounds.

        Parameters
        ----------

        num_input
            The input number
        lower_bound
            The lower boundary
        upper_bound
            The upper boundary
        message
            Appended additional message
    """
    def __init__(self, num_input: float, lower_bound: float, upper_bound: float, message: str = ""):
        self.message = f"'{num_input}' outside of range '{lower_bound}' to '{upper_bound}' inclusive. {message}"
        super().__init__(self.message)
