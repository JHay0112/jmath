'''
    Maths with Units
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .units import Unit
from .conversion import universal, define_alias, define_conversion, UnitSpace
from .annotation import annotate
from .si import si
from .other import other