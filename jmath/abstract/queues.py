'''
    Queue data types.
'''

# - Imports

from .lists import LinkedList
from typing import Any

# - Classes

class Queue(LinkedList):
    """
        Queue Abstract Data Type
    """

    def enqueue(self, data: Any):
        """
            Enqueues a piece of data onto the queue.

            data
                The piece of data to enqueue.
        """
        super().append(data)

    def dequeue(self) -> Any:
        """Returns and removes the first queue item."""
        head = self.head
        self.head = head.next
        return head.data