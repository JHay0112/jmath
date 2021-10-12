'''
    Test Heaps from jmath.abstract
'''

# - Imports

from ..jmath.abstract.heaps import MinBinaryHeap, MaxBinaryHeap
from .tools import random_list, repeat

# - Tests

@repeat
def test_min_heap():
    '''Tests that a min heap sorts as expected'''
    input_list = random_list()
    sorted_list = sorted(input_list)
    heap = MinBinaryHeap()
    heap_sorted_list = []

    for item in input_list:
        heap.push(item)

    while len(heap.items) > 0:
        heap_sorted_list.append(heap.pop())

    assert sorted_list == heap_sorted_list

@repeat
def test_max_heap():
    '''Tests that a max heap sorts as expected'''
    input_list = random_list()
    sorted_list = sorted(input_list, reverse = True)
    heap = MaxBinaryHeap()
    heap_sorted_list = []

    for item in input_list:
        heap.push(item)

    while len(heap.items) > 0:
        heap_sorted_list.append(heap.pop())

    assert sorted_list == heap_sorted_list