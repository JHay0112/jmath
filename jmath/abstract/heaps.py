'''
    Implementation of Heap types
'''

# - Imports

from typing import Optional, List

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

    def children_of(self, index: int) -> Optional[List[int]]:
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

        if children == []:
            children = None

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
        while self.children_of(index) is not None:
            children = self.children_of(index)
            # For two children
            if len(children) == 2:
                # Get child values
                child_vals = [self.items[i] for i in children]
                # Compare values
                child_val = self.compare(child_vals)
                # Get the better
                if self.items[children[0]] == child_val:
                    child = children[0]
                else:
                    child = children[1]
            else:
                # For one child
                child = children[0]
            # Compare child to parent
            best_val = self.compare(self.items[child], self.items[index])
            # If the child is the best
            if best_val == self.items[child]:
                # Swap parent and item
                self.items[index], self.items[child] = self.items[child], self.items[index]
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

        while self.parent_of(index) is not None:
            parent = self.parent_of(index)
            # Compare child and parent
            best_val = self.compare(self.items[index], self.items[parent])
            # If the parent is not the better value
            if best_val != self.items[parent]:
                # Swap parent and item
                self.items[index], self.items[parent] = self.items[parent], self.items[index]
                # Mark parent as next to look at
                index = parent
            else:
                # There is no swap to do, break
                break

    def push(self, value):
        """
            Pushes a value onto the heap

            Parameters
            ----------

            value
                The value to push on
        """
        # Append value
        self.items.append(value)
        # Sift up value
        self.sift_up(len(self.items) - 1)

    def pop(self):
        """
            Pops a value from the heap
        """

        # Get value from top
        top = self.items[0]
        # Put new value on top
        if len(self.items) > 1:
            self.items[0] = self.items.pop()
            # Sift top down
            self.sift_down(0)
        else:
            # Ensure list emptiess
            self.items.pop()

        return top

class MinBinaryHeap(BinaryHeap):
    '''
        Binary Heap with minimum value stored at root.
    '''
    compare = min

class MaxBinaryHeap(BinaryHeap):
    '''
        Binary Heap with maximum value stored at root.
    '''
    compare = max