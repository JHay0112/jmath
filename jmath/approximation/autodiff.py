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

    def __radd__(self, other):

        if isinstance(other, Variable):
            other.log(op.add, other, self)
        self.log(op.add, other, self)

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

        self.inputs = []
        self.func = func
        self.output = Variable(self)

    def input(self, *inputs: Variable):
        '''
            Registers a new input borrowed by the Function.
            Production order determines input order on Function use.

            Parameters
            ----------

            inputs
                The inputs to register
        '''
        if isinstance(inputs[0], (list, tuple)):
            inputs = inputs[0]
        for input in inputs:
            input.input_of.add(self)
            self.inputs.append(input)

    def __call__(self, *inputs: Union[int, float, Uncertainty, Variable, 'Function']) -> Union[int, float, Uncertainty, 'Function']:
        '''Evaluate the function.'''

        if len(inputs) == 0:
            # Called with no inputs
            # Thus we need to pass the variable inputs
            inputs = tuple([input.value for input in self.inputs])
            assert None not in inputs
            return self.func(*inputs)
        elif all(isinstance(input, (Variable, Function)) for input in inputs):
            # If all inputs are functions/variables
            # Clear current inputs
            self.inputs = []
            # Then let's register the inputs
            for input in inputs:
                if isinstance(input, Variable):
                    self.input(input)
                elif isinstance(input, Function):
                    self.input(input.output)
            # Let's return the function for use
            return self

        # Else we have a non-empty, non-variable input
        # Incase a tuple is mistakenly passed.
        if isinstance(inputs[0], tuple):
            inputs = inputs[0]

        # Function must just have been called normally
        # Now iterate through the inputs
        # Setting variables where appropriate
        for i, input in enumerate(inputs):
            if isinstance(self.inputs[i], Variable):
                self.inputs[i].value = input

        # Now call self with updated inputs
        return self()

    def differentiate(self, with_respect_to: int) -> Union['Function', Callable]:

        diff = self.diffs[with_respect_to]

        if isinstance(diff, Function):
            def diff_out(*args):
                return diff(*args) * diff.differentiate(with_respect_to)(*args)
        else:
            def diff_out(*args):
                return diff
            
        return diff_out

# - Definitions

add = Function(op.add)(Variable(), Variable())
mul = Function(op.mul)(Variable(), Variable())