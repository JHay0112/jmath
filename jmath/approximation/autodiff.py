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
        derivatives
            Tuple of partial derivatives of the function with respect to function variables.
    '''
    def __init__(self, func: Callable, derivatives: Tuple[Callable]):

        self.inputs = ()
        self.func = func
        self.derivatives = derivatives

        # Check if diff is not a tuple
        if not isinstance(self.derivatives, tuple):
            # If not then we shall make it one
            self.derivatives = (self.derivatives,)

    def __call__(self):

        if not(isinstance(self.func, Callable)):
            return self.func

        # Input collection
        inputs = []
        for input in self.inputs:
            if isinstance(input, Variable):
                # Variable case
                inputs.append(input.value)
            elif isinstance(input, (int, float, Uncertainty)):
                # Const case
                input.append(input)
            elif isinstance(input, Function):
                # Function case
                inputs.append(input())

        return self.func(*tuple(inputs))

    def __add__(self, other: Supported) -> 'Function':

        if other == 0:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: x + other, 1)
            f.register(self)
            return f
        else:
            # Variable case
            f = Function(op.add, (1, 1))
            f.register(self, other)
            return f

    def __radd__(self, other: Supported) -> 'Function':

        return self + other

    def __sub__(self, other: Supported) -> 'Function':

        if other == 0:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: x - other, 1)
            f.register(self)
            return f
        else:
            # Variable case
            f = Function(op.sub, (1, -1))
            f.register(self, other)
            return f

    def __rsub__(self, other: Supported) -> 'Function':

        if isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: other - x, -1)
            f.register(self)
            return f
        else:
            # Variable case
            f = Function(op.sub, (1, -1))
            f.register(self, other)
            return f

    def __mul__(self, other: Supported) -> 'Function':

        if other == 1:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: other * x, other)
            f.register(self)
            return f
        else:
            # Variable case
            f = Function(op.mul, (lambda x, y: y, lambda x, y: x))
            f.register(self, other)
            return f

    def __pow__(self, power: Union[int, float, Uncertainty]) -> 'Function':

        if power == 1:
            f = Function(lambda x: x, 1)
            f.register(self)
            return f
        elif power == 0:
            return 1
        else:
            # Non-trivial case
            f = Function(lambda x: x**power, lambda x: power*x**(power - 1))
            f.register(self)
            return f

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
            f = Function(lambda x: x/other, 1/other)
            f.register(self)
            return f
        else:
            # Variable case
            f = Function(op.truediv, (lambda x, y: 1/y, lambda x, y: -x/(y**2)))
            f.register(self, other)
            return f

    def __rtruediv__(self, other: Supported) -> 'Function':

        if isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            f = Function(lambda x: other/x, lambda x: -other/(x**2))
            f.register(self)
            return f
        else:
            # Variable case
            f = Function(op.rtruediv, (lambda x, y: 1/y, lambda x, y: -x/(y**2)))
            f.register(self, other)
            return f

    def register(self, *inputs: 'Function'):
        '''
            Registers inputs to the function.

            Parameters
            ----------

            inputs
                Args, the functions to register as inputs. 
        '''
        self.inputs = inputs

    def differentiate(self, wrt: 'Variable') -> 'Function':
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
            partial = Function(self.derivatives[i], None)
            partial.register(*self.inputs)
            func += partial * input.differentiate(wrt)

        return func

class Variable(Function):
    '''
        Variables for function differentiation.
    '''
    def __init__(self):

        super().__init__(lambda x: x, 1)
        self.value = 0
        self.inputs = None
        self.derivatives = None

    def differentiate(self, wrt: 'Variable') -> int:
        
        if wrt == self:
            return 1
        else:
            return 0