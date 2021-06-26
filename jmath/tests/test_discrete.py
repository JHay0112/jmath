"""
    jmath/tests/test_discrete.py

    Runs tests on discrete component using pytest

    Author: Jordan Hay
    Date: 2021-06-25
"""

# - Imports

from ..discrete import *

# - Functions

def test_add_neighbour():
    """Test that adding a neighbour to a node works correctly"""
    node1 = Node("A")
    node2 = Node("B")
    node1.add_neighbour(node2)

    assert node1.neighbours_list()[0] == node2

def test_remove_neighbour():
    """Test that removing a neighbour works"""
    node1 = Node("A")
    node2 = Node("B")
    node1.add_neighbour(node2, two_way=True)
    node1.remove_neighbour(node2)
    # Remove should only remove neighbour from node 1
    assert node1.neighbours_list() == []
    assert node2.neighbours_list()[0] == node1

def test_two_way_neighbour():
    """Test that adding neighbours two ways works"""
    node1 = Node("A")
    node2 = Node("B")
    node1.add_neighbour(node2, two_way=True)

    assert node1.neighbours_list()[0] == node2
    assert node2.neighbours_list()[0] == node1

def test_get_node():
    """Tests that getting a node by ID from a graph works"""
    # Create a looped directional graph
    graph = Graph()
    # Nodes
    nodes = [
        Node("A", 3),
        Node("B", 2),
        Node("C", 1)
    ]
    # Add nodes to graph
    graph.add_nodes(nodes)

    assert graph.get_node("B") == nodes[1]

def test_intersections():
    """Tests whether the intersections method returns only intersections"""
    # Create a looped directional graph
    graph = Graph()
    # Nodes
    nodes = [
        Node("A", 3),
        Node("B", 2),
        Node("C", 1)
    ]
    # Define node relationships
    nodes[0].add_neighbour(nodes[1], 1)
    nodes[1].add_neighbour(nodes[2], 2)
    # Node C gets two neighbours, thus is an intersection
    nodes[2].add_neighbour(nodes[0], 3)
    nodes[2].add_neighbour(nodes[1], 4)
    # Add nodes to graph
    graph.add_nodes(nodes)

    assert graph.intersections() == [nodes[2]]

def test_loops():
    """Tests that loops are generated from a graph as expected"""
    # Create a looped directional graph
    graph = Graph()
    # Nodes
    nodes = [
        Node("A", 3),
        Node("B", 2),
        Node("C", 1)
    ]
    # Define node relationships
    nodes[0].add_neighbour(nodes[1], 1)
    nodes[1].add_neighbour(nodes[2], 2)
    nodes[2].add_neighbour(nodes[0], 3)
    # Add nodes to graph
    graph.add_nodes(nodes)
    # Create a loop that should be identical to generated loop from graph
    loop = Loop(nodes)

    assert graph.loops()[0].relationships() == loop.relationships()

def test_reorder():
    """Tests reordering loops"""
    # Nodes
    nodes = [
        Node("A", 3),
        Node("B", 2),
        Node("C", 1)
    ]
    # Reorder for C at start
    reordered_nodes = [
        nodes[2],
        nodes[0],
        nodes[1]
    ]
    # Create loop off standard nodes
    loop = Loop(nodes)
    # Reorder to have C at start
    loop.reorder(nodes[2])

    assert loop.nodes == reordered_nodes
