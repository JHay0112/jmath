'''
    Automatic Differentiation
'''

# - Imports

import operator as op
from ..uncertainties import Uncertainty
from typing import Union, Callable

# - Globals

'''
    A map of common functions and their partial derivates.
    Partial derivatives are with respect to their positional relative parameter.
'''
diff_map = {
    op.add: (1, 1),
    op.sub: (1, 1),
    op.mul: (
        lambda x, y: y, 
        lambda x, y: x
    ),
    op.truediv: (
        lambda x, y: 1/y,
        lambda x, y: -x/(y**2)
    )
}

# - Classes

class Variable:
    '''
        Allows a function to be applied to a variable input.

        Parameters
        ----------

        func
            The function that owns (outputs to) the variable.
    '''
    def __init__(self, func: 'Function' = None):

        self.output_of = func
        self.input_of = set()
        self.value = None

    def differentiate(self):
        '''Differentiate the Variable'''
        return 1

class Function:
    '''
        A Differentiable Function.

        Parameters
        ----------

        func
            The callable function to be represented.
    '''
    def __init__(self, func: Callable):

        self.vars = []
        self.func = func
        self.output = Variable(self)

    def __call__(self, *inputs: Union[int, float, Uncertainty, Variable, 'Function']) -> Union[int, float, Uncertainty, 'Function']:
        '''Evaluate the function.'''

        if len(inputs) == 0:
            # Use existing values
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
            # Normal call
            # We need to find the root functions and set their variables before setting ours
            for i, var in enumerate(self.vars):
                if var.output_of is not None:
                    var.output_of(*inputs)
                else:
                    var.value = inputs[i]

            return self()

# - Definitions

add = Function(op.add)
mul = Function(op.mul)
