import pdb
from typing import List


class Node:

    def __init__(self, left, right, key: int):
        self.left = left
        self.right = right
        self.key = key
        
        self.left_count = 0


class Tree:
    def __init__(self):
        self.root = None 
    
    def add_node(self, key: int):
        if self.root is None:
            self.root = Node(None, None, key)
        elif self.root.key == key:
            return
        else:
            self._recursive_add(self.root, key)

    def _recursive_add(self, node: Node, key: int):
        if node.key > key:
            self._add_left_node(node, key)
        elif node.key < key:
            self._add_right_node(node, key)
        
    def _add_left_node(self, node: Node, key: int):
        node.left_count += 1
        if node.left is None:
            node.left = Node(None, None, key)
        elif node.left.key == key:
            return 
        else:
            self._recursive_add(node.left, key)

    def _add_right_node(self, node: Node, key: int):
        if node.right is None:
            node.right = Node(None, None, key)
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

    def inorder_walk(self, node: Node, nodes: List[Node] = []) -> List[Node]:
        if node:
            self.inorder_walk(node.left, nodes)
            nodes.append(node)
            self.inorder_walk(node.right, nodes)
    
    def inorder_walk_reverse(self, node: Node, nodes: List[Node] = []) -> List[Node]:
        if node:
            self.inorder_walk_reverse(node.right, nodes)
            nodes.append(node)
            self.inorder_walk_reverse(node.left, nodes)

    def rotate_left(self, node: Node):
        reversed_node = node.right
        node.right = reversed_node.left
        reversed_node.left = node
        return reversed_node
    
    def rotate_right(self, node: Node):
        reversed_node = node.left
        node.left = reversed_node.right
        reversed_node.right = node
        return reversed_node
    
    def is_balanced(self, node: Node) -> bool:
        return self.height(node.left) == self.height(node.right)

    def height(self, node: Node) -> int:
        if not node:
           return 0
        return 1 + max(self.height(node.right), self.height(node.left))

    def balance_node(self, node: Node) -> Node:
        diff = self._bfactor(node)
        while(diff != 0):
            node = self._rotations(node, diff)
            diff = self._bfactor(node)
        if node.left:
            node.left = self.balance_node(node.left)
        if node.right:
            node.right = self.balance_node(node.right) 
        return node

    def _bfactor(self, node: Node) -> int:
        left_height =  0 if not node.left else self.height(node.left)
        right_height = 0 if not node.right else self.height(node.right)
       	return left_height - right_height
    
    def _rotations(self, node: Node, diff: int) -> Node:
        if diff == 0:
            return node
        elif diff > 0:
            if self._bfactor(node.left) < 0:
                node = self.rotate_left(node.left)
            node = self.rotate_right(node)
        else:
            if self._bfactor(node.right) > 0:
               node.right = self.rotate_right(node.right)
            node = self.rotate_left(node) 
        return node
      
    def find_k_element(self, k: int) -> int: 
        element_value = -1
        if self.root: 
            current = self.root
            while current:
                if current and current.left_count + 1 == k:
                    element_value = current.key
                    current = None
                elif k > current.left_count:
                    k = k - current.left_count + 1
                    current = current.right
                else:
                    current = current.left
        return element_value
