'''
    Cryptography tools.

    Default Packages
    ----------------

    jmath.cryptography.affine
        Provides tools for using affine ciphers
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .affine import Affine