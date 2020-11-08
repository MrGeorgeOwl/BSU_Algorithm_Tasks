import pytest

from binary_search_tree import Tree, child_count


@pytest.fixture
def balanced_tree():
    tree = Tree()
    tree.add_node(4)

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


def test_balance_by_kth_min_element(unbalanced_tree):
    balanced_node = unbalanced_tree.balance_by_kth_min_element(
        unbalanced_tree.root)
    assert unbalanced_tree.is_balanced(balanced_node)


def test_left_count(balanced_tree):
    assert child_count(balanced_tree.root.left) == 3


def test_right_count(balanced_tree):
    assert child_count(balanced_tree.root.right) == 3


@pytest.mark.parametrize("k", [3, 2, 4])
def test_k_min_element(k, balanced_tree):
    assert balanced_tree.find_k_element(
        balanced_tree.root, k).key == k
