'''
    jmath/physics/__init__.py

    Tools for physical simulations. By default includes mechanics and prefixes.

    Default Packages
    ----------------

    jmath.physics.mechanics
        Provides tools for modelling mechanical systems, particularly static systems with gravity and electromagnetism.
    jmath.physics.prefixes
        Set of SI prefixes used in physics.

    Optional Packages
    -----------------

    jmath.physics.circuits
        Circuit modelling based on jmath.discrete. In development. Not provided by default.
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .mechanics import PhysObj, PhysEnv
from .prefixes import *