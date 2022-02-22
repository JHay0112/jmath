'''
    Automatic Differentiation
'''

# - Imports

import operator as op
from ..uncertainties import Uncertainty
from typing import Union, Callable, Tuple

# - Typing

Supported = Union[int, float, Uncertainty, 'Function', 'Variable']

# - Classes

class Variable:
    '''
        Allows a function to be applied to a variable input.
    '''
    def __init__(self):

        self.output_of = None
        self.input_of = set()
        self.value = None

    def __add__(self, other: Supported) -> 'Function':

        if other == 0:
            # Special case
            return self
        elif isinstance(other, (int, float, Uncertainty)):
            # Numeric case
            return Function(lambda x: x + other, lambda x: 1)
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
            return Function(lambda x: other * x, lambda x, y: other)
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

class Function(Variable):
    '''
        A Differentiable Function.

        Parameters
        ----------

        func
            The callable function to be represented.
        diff
            A tuple of functions produced upon differentiation with respect to the function variables.
    '''
    def __init__(self, func: Callable, diff: Tuple[Callable]):

        self.vars = []
        self.func = func
        self.diff = diff
        self.output = Variable()
        self.output.output_of = self

        # Check if diff is not a tuple
        if not isinstance(diff, tuple):
            # If not then we shall make it one
            self.diff = (diff,)

    def __call__(self, *inputs: Union[int, float, Uncertainty, Variable, 'Function']) -> Union[int, float, Uncertainty, 'Function']:
        '''Evaluate the function.'''

        if len(inputs) == 0:
            # Call inner functions
            for var in self.vars:
                if var.output_of is not None:
                    var.output_of()
            # Use var values
            inputs = tuple(var.value for var in self.vars)
            # Now execute the function
            self.output.value = self.func(*inputs)
            return self.output.value
        elif all(isinstance(input, (Variable, Function)) for input in inputs):
            # If all inputs are functions/variables
            # Clear current inputs
            self.vars = []
            # Then let's register the inputs
            for input in inputs:
                if isinstance(input, Variable):
                    self.vars.append(input)
                    input.input_of.add(self)
                elif isinstance(input, Function):
                    self.vars.append(input.output)
                    input.output.input_of.add(self)
            # Let's return the function for use
            return self
        else:
            # Real inputs
            # Evaluate the function
            return self.func(*inputs)

    def differentiate(self, var: Variable) -> 'Function':
        '''
            Produces the partial differential of the function with respect to the specified variable.

            Parameters
            ----------

            var
                The variable to differentiate with repsect to.
        '''
        # Derivative produced
        func = 0
        # Go down each 'branch'
        for i, input_var in enumerate(self.vars):
            branch = self.diff[i]
            # Check if it is 'owned' by a function
            if input_var.output_of is not None:
                # Then derive that function by the same variable and add it
                func += branch * input_var.output_of.differentiate(var)
            else:
                func = branch
        
        return func