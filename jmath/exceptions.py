"""
    Defines jmath exceptions

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Classes

class VectorsNotSameSize(Exception):

    def __init__(self):
        """Exception throw for operations on vectors of different sizes"""
        self.message = "Operation invalid for vectors of different sizes."
        super().__init__(self.message)