"""
    jmath/exceptions.py

    Defines jmath exceptions

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Classes

class VectorsNotSameSize(Exception):

    def __init__(self, message = "Operation invalid for vectors of different sizes."):
        """Exception throw for operations on vectors of different sizes"""
        self.message = message
        super().__init__(self.message)