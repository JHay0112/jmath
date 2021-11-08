'''
    Maths with Units
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .units import Unit
from .conversion import define_conversion, define_alias
from .annotation import annotate