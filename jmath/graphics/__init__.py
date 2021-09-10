"""
    Graphics module
"""

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .windows import Window, Canvas
from .shapes import Shape, Rectangle, Circle