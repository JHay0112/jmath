'''
    Automatic Differentiation
'''

# - Imports

import operator as op
import inspect
import string
from functools import wraps
from types import FunctionType
from .uncertainties import Uncertainty
from typing import Any, Union, Callable, Tuple

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
            Note that derivatives may be numeric values or functions with built-in operations and Functions.
    '''
    def __init__(self, func: Callable, derivatives: Tuple[Callable]):

        self.inputs = None
        self.func = func
        self.derivatives = derivatives

        # Check if diff is not a tuple
        if not isinstance(self.derivatives, tuple):
            # If not then we shall make it one
            self.derivatives = (self.derivatives,)

    def __str__(self):

        # Get parameters
        params = tuple()
        if self.inputs is not None:
            params = tuple(str(input) for input in self.inputs)

        # Cases for operations
        if self.func == op.mul:
            return f"{params[0]}*{params[1]}"
        elif self.func == op.truediv:
            return f"{params[0]}/{params[1]}"
        elif self.func == op.sub:
            return f"{params[0]}-{params[1]}"
        elif self.func == op.add:
            return f"{params[0]}+{params[1]}"

        # Standard function
        return f"{self.func.__name__}{str(params)[:-2]})"

    def __call__(self, **kwargs):

        if not isinstance(self.func, Callable):
            return self.func

        # Input collection
        inputs = []
        # Start computing inputs
        for input in self.inputs:
            if isinstance(input, Variable):
                # Variable case
                # Check if the variable has been assigned a value
                if input.id in kwargs.keys():
                    inputs.append(kwargs[input.id])
                else:
                    # There is no value for the variable???
                    # Throw a value error
                    raise KeyError(f"Variable '{input.id}' was not assigned a value on function call!")
            elif isinstance(input, (int, float, Uncertainty)):
                # Const case
                input.append(input)
            elif isinstance(input, Function):
                # Function case
                inputs.append(input(**kwargs))

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
            f = Function(op.sub, (-1, 1))
            f.register(self, other)
            return f

    def __mul__(self, other: Supported) -> 'Function':

        if other == 1:
            # Special case
            return self
        elif other == 0:
            return 0
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

    def __neg__(self) -> 'Function':

        f = Function(op.neg, -1)
        f.register(self)
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

    def differentiate(self, wrt: Union['Variable', str]) -> 'Function':
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
            partial = self.derivatives[i]
            if isinstance(partial, FunctionType):
                partial = partial(*self.inputs)
            func += partial * input.differentiate(wrt)

        return func

    @wraps(differentiate)
    def d(self, wrt: Union['Variable', str]) -> 'Function':
        return self.differentiate(wrt)

class Variable(Function):
    '''
        Variables for function differentiation.

        Parameters
        ----------

        id
            Unique identifier string.
    '''
    def __init__(self, id: str = None):

        super().__init__(lambda x: x, None)
        self.id = id
        self.inputs = None
        self.derivatives = None

    def __str__(self):

        return self.id

    def __call__(self, input: Any) -> Any:

        return input

    def differentiate(self, wrt: 'Variable') -> int:
        
        if ((wrt == self) or (wrt == self.id and self.id is not None)):
            return 1
        else:
            return 0

# - Functions

def analyse(f: Callable) -> Function:
    '''
        Automatically analyses the given function and produces a Function object.

        Parameters
        ----------

        f
            The function to analyse

        Returns
        -------

        Function
            A differentiable function object representing the given function.
    '''
    # Get the list of parameters from the function
    names = inspect.getargspec(f)[0]
    # Convert these into variables for the function
    vars = tuple(Variable(name) for name in names)
    # Pass these to the function
    f = f(*vars)
    # Register the input variables
    f.register(*vars)
    # And return
    return f

# - Main

# Define all english letters as 'Variable's
# This code is very silly
# I'm not sure it should stay here
for letter in string.ascii_letters:
    globals()[letter] = Variable(letter)