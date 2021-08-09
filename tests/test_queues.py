"""
    Tests Queue Abstract Data Types
"""

# - Imports

from ..jmath.abstract.queues import Queue

# - Tests

def test_enqueue_dequeue():
    """Tests queues and dequeueing."""
    data = [3, 2, 1]
    q = Queue()
    
    # Enqueue
    for item in data:
        q.enqueue(item)

    # Dequeue
    for i in range(len(data)):
        assert data[i] == q.dequeue()

def test_listify():
    """Tests that a queue list is generated as expected."""
    data = [3, 2, 1]
    q = Queue()
    
    # Enqueue
    for item in data:
        q.enqueue(item)

    lst = q.list()

    assert lst == data