'''
    Implementation of Heap types
'''

# - Imports

from typing import Optional, Union, List

# - Classes

class BinaryHeap:
    '''
        Implementation of a Generic Binary Heap
    '''
    def __init__(self):

        self.items = []

    def parent(self, index: int) -> Optional[int]:
        '''
            Calculates the location of the parent of a node

            Parameters
            ----------

            index
                The index to calculate the parent of

            Returns
            -------

            The index of the parent node or None if it does not have a parent
        '''

        if index == 0:
            return None
        else:
            # Calculate and return parent index
            return (index - 1)//2

    def children(self, index: int) -> Optional[Union[List[int, int], List[int]]]:
        '''
            Calculates the locations of the children of a node

            Parameters
            ----------

            index
                The index of to find the children of

            Returns
            -------

            An iterable containing the indices of the child nodes
        '''

        # Calculate candidate indices
        child1 = 2*index + 1
        child2 = 2*index + 2
        children = []

        # Check children in heap
        if child1 < len(self.items):
            children.append(child1)
        
        if child2 < len(self.items):
            children.append(child2)

        # Return as tuple
        return children