'''
    The jmath top level package. Provides a set of default and optional sub-packages for doing maths in Python.

    Default Packages
    ----------------

    jmath.uncertainties
        Provides the Uncertainty object which gives the capability for calculations that use values with associated uncertainties.
    jmath.linearalgebra
        Provides Vector, Point, and Line objects for linear algebra based calculations.

    Optional Packages
    -----------------

    jmath.discrete
        In development programming representation of Nodes and Graphs.
    
    jmath.physics
        Tools for physical simulations. By default includes mechanics and prefixes.

        jmath.physics.mechanics
            Provides tools for modelling mechanical systems, particularly static systems with gravity and electromagnetism.
        jmath.physics.circuits
            Circuit modelling based on jmath.discrete. In development. Not provided by default.
        jmath.physics.prefixes
            Set of SI prefixes used in physics.
    
    jmath.approximation
        Tools for approximating mathematical equations.

        jmath.approximation.euler_method
            The euler method for approximating the integrals of differential equations.

    jmath.abstract
        Implementations of Abstract Data Types.

    jmath.modular
        Simple functions for working with modular arithmetic

    jmath.cryptography
        Tools for working with cryptography. By default includes the affine cipher.

        jmath.cryptography.affine
            Affine cipher object for encrypting/decrypting affine.

    Testing
    -------

    Testing can be performed upon the entire jmath codebase using

        $ pytest

    when in the jmath root directory.

    Documentation
    -------------

    Upon addition of a new sub-module the documentation must be updated with

        $ sphinx-apidoc -o ./docs/source/ ./jmath

    when in the jmath root directory.

    Documentation is automatically built by a workflow in github and published to https://jordanhay.com/jmath
        
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .uncertainties import Uncertainty
from .linearalgebra import Vector, Point, Line
from .modular import extended_gcd, modular_inverse