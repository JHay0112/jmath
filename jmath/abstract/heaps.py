'''
    Implementation of Heap types
'''

# - Imports

from typing import Optional, Union, List

# - Classes

class BinaryHeap:
    '''
        Implementation of a Generic Binary Heap

        Attributes
        ----------

        compare : Callable
            Defines the comparison operator for the heap, should take a set of values and return one per an ordering. 
            For example the comparison operator for a min heap is the min function.
    '''

    compare = None

    def __init__(self):

        self.items = []

    def parent_of(self, index: int) -> Optional[int]:
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

    def children_of(self, index: int) -> Optional[Union[List[int, int], List[int]]]:
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

    def sift_down(self, index: int):
        """
            Performs a sift down operation on a given index

            Parameters
            ----------

            index
                The index to perform the sift down operation on
        """

        # While there are children
        while children := self.children_of(index) is not None:
            # For two children
            if len(children) == 2:
                # Get child values
                child_vals = [self.items[i] for i in children]
                # Compare values
                child_val = self.compare(child_vals)
                # If child 1 matches
                if self.items[children[0]] == child_val:
                    child = children[0]
                else:
                    child = children[1]
            else:
                # For one child
                child = children[0]
            # Compare child to parent
            best_val = self.compare(self.items[child], self.items[index])
            # If the child is the in order value
            if best_val == self.items[child]:
                # Swap parent and item
                self.items[index], self.items[child] == self.items[child], self.items[index]
                # Mark child index as new index to look at 
                index = child
            else:
                # Else there is no swap to do, break
                break

    def sift_up(self, index: int):
        """
            Performs a sift up operation on a given index

            Parameters
            ----------

            index
                The index to perform the sift up operation on
        """

        while parent := self.parent_of(index) is not None:
            # Compare child and parent
            best_val = self.compare(self.items[index], self.items[parent])
            # If the parent is the better value
            if best_val == self.items[parent]:
                # Swap parent and item
                self.items[index], self.items[parent] == self.items[parent], self.items[index]
                # Mark parent as next to look at
                index = parent
            else:
                # There is no swap to do, break
                break