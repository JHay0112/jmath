'''
    List data types.
'''

# - Imports

from typing import Any

# - Classes

class Node:
    """
        Node of a list.

        Parameters
        ----------

        data
            Data stored by the node.
        next
            Reference to next piece node of the list.
    """
    def __init__(self, data: Any, next: "Node" = None):
        
        self.data = data
        self.next = next

    def append(self, node: "Node"):
        """
            Appends a node to the back of this node.
            
            Parameters
            ----------
            
            node
                Node to be appended.
        """
        node.next = self.next
        self.next = node

class BiNode(Node):
    """
        Node that can refer to objects in front and behind it.

        Parameters
        ----------

        data
            Data stored by the node.
        next
            Reference to next piece node of the list.
        prev
            Reference to previous node in the list.
    """
    def __init__(self, data: Any, next: "BiNode" = None, prev: "BiNode" = None):

        self.prev = prev

        super().__init__(data, next)

class LinkedList:
    """
        Linked List abstract data type.
    """
    def __init__(self):

        self.head = None
        self.bottom = None

    def __iter__(self):
        """Iterate through List."""
        # Get start
        current = self.head
        # While the current object is not none
        while current != None:
            # Yield the current object's data
            yield current.data
            # Update current
            current = current.next

    def append(self, data: Any):
        """
            Appends a node to the end of the list. O(1).

            Parameters
            ----------

            data
                The data to be appended.
        """
        node = Node(data)

        if self.bottom == None:
            # No node in the bottom.
            self.bottom = node
            self.head = node
        else:
            # List initialised
            # Append to current bottom node
            self.bottom.append(node)
            # Replace bottom node
            self.bottom = node

    def extend(self, list: "LinkedList"):
        """
            Extends list. O(1).

            Parameters
            ----------
            
            list
                List to be appended onto this list.
        """

        self.append(list.head.data)
        self.bottom = list.bottom

    def insert(self, index: int, data: Any):
        """
            Inserts data at the specified index into the list. O(index) operation.
            Negative indices other than -1 unsupported.

            index
                Index for data to be inserted at.
            data
                Data to be inserted.
        """

        node = Node(data)

        if index == 0:
            # Head
            node.append(self.head)
            self.head = node
        elif index == -1:
            # Bottom
            self.bottom.append(node)
            self.bottom = node
        elif index < -1:
            # No support for negative indexes.
            raise IndexError()
        else:
            # Somewhere else, iterate!
            i = 0
            for item in self:
                if i == index:
                    item.append(node)
                    return
                else:
                    i += 1
