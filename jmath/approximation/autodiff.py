'''
    Automatic Differentiation.
'''

# - Imports

from typing import Callable, Tuple, TypeVar

# - Typing

Numeric = TypeVar("Numeric", float, int, "Variable")

# - Classes

class Variable:
    '''
        Represents a variable in a function for automatic differentiation.
    '''
    pass

class OperatorNode:
    '''
        Node representing an operation in the graph.

        Parameters
        ----------

        operation
            The operation the node represents
    '''
    def __init__(self, operation: Callable[[float], float], values = Tuple[Numeric, Numeric]):

        self.operation = operation
        self.values = values

    def __repr__(self):
        '''Programming Representation'''
        return f"OperatorNode({self.operation.__name__}, ({self.values[0]}, {self.values[1]}))"

    def __str__(self):
        '''String Representation'''
        return f"{self.operation.__name__}({self.values[0]}, {self.values[1]})"