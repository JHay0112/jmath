'''
    "Loud" Mathematical Functions
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .modular import gcd, modular_inverse_brute_force
from .primes import primality, relative_primality
from .graphs import prufer_solver