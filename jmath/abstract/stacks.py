'''
    Stack Abstract Data Type
'''

# - Imports

from typing import Any

# - Classes

class Stack:
    """
        Stack Abstract Data Type
    """
    def __init__(self):
        
        self.stack = []

    def pop(self) -> Any:
        """Removes and returns the top item from the stack."""
        return self.stack.pop()

    def push(self, item: Any):
        """
            Adds a new item on top of the stack.

            Parameters
            ----------

            item
                The item to be added to the stack
        """

        self.stack.append(item)

    def peek(self):
        """Returns the top item of the stack without removing."""
        return self.stack[-1]