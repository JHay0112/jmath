'''
    Automatic Differentiation
'''

# - Imports

import operator as op
from ..uncertainties import Uncertainty
from typing import Union, Callable, Tuple

# - Typing

Supported = Union[int, float, Uncertainty, 'Function', 'Variable']
Numeric = Union[int, float, Uncertainty]

# - Classes

class Function:
    '''
        Automatic Differentiation Function Object

        Parameters
        -----------

        func
            Represented function.
        diff
            Tuple of partial derivatives of the function.
    '''
    def __init__(self, func: Callable, diff: Tuple[Callable]):

        self.inputs = []
        self.func = func
        self.diff = diff

        # Check if diff is not a tuple
        if not isinstance(diff, tuple):
            # If not then we shall make it one
            self.diff = (diff,)

    def __add__(self, other: Supported) -> 'Function':

        if other == 0:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: x + other, lambda x: 1)
            f.register(self)
            return f
        else:
            # Variable case
            return Function(op.add, (lambda x, y: 1, lambda x, y: 1))

    def __radd__(self, other: Supported) -> 'Function':

        return self + other

    def __sub__(self, other: Supported) -> 'Function':

        if other == 0:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            return Function(lambda x: x - other, lambda x: 1)
        else:
            # Variable case
            return Function(op.sub, (lambda x, y: 1, lambda x, y: -1))

    def __rsub__(self, other: Supported) -> 'Function':

        if isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            return Function(lambda x: other - x, lambda x: -1)
        else:
            # Variable case
            return Function(op.sub, (lambda x, y: 1, lambda x, y: -1))

    def __mul__(self, other: Supported) -> 'Function':

        if other == 1:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: other * x, lambda x, y: other)
            f.register(self)
            return f
        else:
            # Variable case
            return Function(op.mul, (lambda x, y: y, lambda x, y: x))

    def __rmul__(self, other: Supported) -> 'Function':

        return self * other

    def __truediv__(self, other: Supported) -> 'Function':

        if other == 1:
            # Special case
            return other
        elif other == 0:
            # Error case
            raise ZeroDivisionError
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            return Function(lambda x: x/other, lambda x: 1/other)
        else:
            # Variable case
            return Function(op.truediv, (lambda x, y: 1/y, lambda x, y: -x/(y**2)))

    def __rtruediv__(self, other: Supported) -> 'Function':

        if isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            return Function(lambda x: other/x, lambda x: -other/(x**2))
        else:
            # Variable case
            return Function(op.rtruediv, (lambda x, y: 1/y, lambda x, y: -x/(y**2)))

    def register(self, *inputs: 'Function', clear: bool = True):
        '''
            Registers inputs to the function.

            Parameters
            ----------

            inputs
                Args, the functions to register as inputs. 
            clear
                Clear function inputs before registering.
        '''
        if clear:
            self.inputs = []
        for input in inputs:
            self.inputs.append(input)

    def differentiate(self, wrt: 'Variable') -> Callable:
        '''
            Differentiates the function with respect to a variable.

            Parameters
            ----------

            wrt
                The variable to differentiate with respect to.
        '''
        # The differentiated function
        func = 0
        # Move across inputs
        for i, input in enumerate(self.inputs):
            # Get respective derivative
            partial = Function(self.diff[i], lambda x: 1)
            func += partial * input.differentiate(wrt)

        return func

class Variable(Function):
    '''
        Variables for function differentiation.
    '''
    def __init__(self):

        super().__init__(lambda x: x, lambda x: 1)