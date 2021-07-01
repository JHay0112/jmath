"""
    jmath/exceptions.py

    Defines jmath exceptions

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Imports

import copy

# - Classes

class VectorsNotSameSize(Exception):
    """Exception throw for operations on vectors of different sizes"""
    def __init__(self, message = "Operation invalid for vectors of different sizes."):
        self.message = message
        super().__init__(self.message)