import pdb
import pytest

from binary_search_tree import Tree, Node

@pytest.fixture
def balanced_tree():
    tree = Tree()
    tree.root = Node(None, None, 4)

    tree.add_node(2)
    tree.add_node(1)
    tree.add_node(3)

    tree.add_node(6)
    tree.add_node(5)
    tree.add_node(7)
    
    return tree

@pytest.fixture
def unbalanced_tree():
    tree = Tree()
    # for i in range(1, 8):
    #    tree.add_node(i)
    tree.add_node(1)
    tree.add_node(2)
    tree.add_node(9)
    tree.add_node(6)
    tree.add_node(7)
    tree.add_node(4)
    tree.add_node(10)
    return tree


def test_balanced_tree(balanced_tree):
    assert balanced_tree.is_balanced(balanced_tree.root)


def test_search(balanced_tree):
    assert balanced_tree.search_key(balanced_tree.root, 2).key == 2


def test_inorder_walk(balanced_tree):
    nodes = []
    balanced_tree.inorder_walk(balanced_tree.root, nodes)    
    nodes = [node.key for node in nodes]
    assert nodes == [i for i in range(1, 8)]


def test_inorder_walk_reverse(balanced_tree):
    nodes = []
    balanced_tree.inorder_walk_reverse(balanced_tree.root, nodes)
    nodes = [node.key for node in nodes]
    assert nodes == list(reversed([i for i in range(1, 8)]))


def test_unbalanced_tree(unbalanced_tree):
    assert not unbalanced_tree.is_balanced(unbalanced_tree.root)


def test_balance_node(unbalanced_tree):
    balanced_node = unbalanced_tree.balance_node(unbalanced_tree.root)
    assert unbalanced_tree.is_balanced(balanced_node)


@pytest.mark.parametrize("k, exp_value", [
    (2, 1),
    (3, 1),
    (0, 4),
])
def test_min_k_node(k, exp_value, balanced_tree):
    min_k_node = balanced_tree.min_k_key(k)
    assert min_k_node.key == exp_value
