'''
    Tests abstract list data types.
'''

# - Imports

from ..jmath.abstract.lists import Node, BiNode, LinkedList

# - Tests

def test_nodes():
    """Tests raw node objects and their interaction."""

    n1 = Node("a")
    n2 = Node("b")
    # Append n2 to n1
    n1.append(n2)

    assert n1.next == n2
    assert n2.next == None

def test_binode_append():
    """Tests binode append."""

    n1 = BiNode("a")
    n2 = BiNode("b")
    # Append n2 to n1
    n1.append(n2)

    assert n1.next == n2
    assert n2.prev == n1

    assert n1.prev == None
    assert n2.next == None

def test_binode_prepend():
    """Tests binode prepend."""

    n1 = BiNode("a")
    n2 = BiNode("b")
    # Prepend n1 to n2
    n2.prepend(n1)

    assert n1.next == n2
    assert n2.prev == n1

    assert n1.prev == None
    assert n2.next == None

def test_linked_list_iter():
    """Tests linked list iteration."""

    list = LinkedList()
    # Fill list with subsequent numbers
    for i in range(0, 100):
        list.append(i)

    # Iterate through list
    i = 0
    for item in list:
        # Assert i is equivalent to the item
        assert i == item
        i += 1