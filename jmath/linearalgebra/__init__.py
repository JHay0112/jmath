'''
    Linear Algebra Tools

    Default Packages
    ----------------

    
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .vectors import Vector
from .points import Point, Complex
from .lines import Line
from .planes import Plane