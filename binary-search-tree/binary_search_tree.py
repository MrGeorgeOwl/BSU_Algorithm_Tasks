from typing import List

class Node:

    def __init__(self, parent, left, right, key: int):
        self.parent = parent
        self.left = left
        self.right = right
        self.key = key


class Tree:
    def __init__(self):
        self.head = None 

    def build(self, numbers: List[int]):
        middle = int(len(numbers) / 2)
        self.head = Node(None, None, None, numbers[middle])
        for index, item in enumerate(numbers):
            if index == middle:
                continue
            self.add_node(item) 
    
    def add_node(self, key: int):
        if self.head is None:
            self.head = Node(None, None, None, key)
        elif self.head.key == key:
            return
        else:
            self._recursive_add(self.head, key)

    def _recursive_add(self, node: Node, key: int):
        if node.key > key:
            self._add_left_node(node, key)
        elif node.key < key:
            self._add_right_node(node, key)
        
    def _add_left_node(self, node: Node, key: int):
        if node.left is None:
            node.left = Node(node, None, None, key)
        elif node.left.key == key:
            return 
        else:
            self._recursive_add(node.left, key)

    def _add_right_node(self, node: Node, key: int):
        if node.right is None:
            node.right = Node(node, None, None, key)
        elif node.right.key == key:
            return
        else:
            self._recursive_add(node.right, key)
    
    def search_key(self, node: Node, key: int) -> Node:
        if not node or node.key == key:
            return node
        
        if node.key < key:
            return self.search_key(node.right, key)
        else:
            return self.search_key(node.left, key)

    def inorder_walk(self, node: Node) -> Node:
        if node:
            self.inorder_walk(node.left)
            print(node.key, end=' ')
            self.inorder_walk(node.right) 

