'''
    Abstract Data Types from Computer Science.
'''

# - Namespace

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# - Defaults

from .stacks import Stack
from .lists import LinkedList
from .queues import Queue
from .heaps import MaxBinaryHeap, MinBinaryHeap