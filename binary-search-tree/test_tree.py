from binary_search_tree import Tree, Node

def test_search():
    array = list(range(1, 11))    
    tree = Tree()
    tree.build(array)
    print()
    tree.inorder_walk(tree.head)
    assert tree.search_key(tree.head, 2).key == 2

