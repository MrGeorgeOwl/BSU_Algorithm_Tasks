from typing import List, Optional, Tuple, Union


class Node:

    def __init__(self, left, right, key: int):
        self.left = left
        self.right = right
        self.key = key

        self.left_childs_count = 0
        self.right_childs_count = 0


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
        node.left_childs_count += 1
        if node.left is None:
            node.left = Node(None, None, key)
        elif node.left.key == key:
            return
        else:
            self._recursive_add(node.left, key)

    def _add_right_node(self, node: Node, key: int):
        node.right_childs_count += 1
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

    def inorder_walk_reverse(
        self, node: Node, nodes: List[Node] = []
    ) -> List[Node]:
        if node:
            self.inorder_walk_reverse(node.right, nodes)
            nodes.append(node)
            self.inorder_walk_reverse(node.left, nodes)

    def _rotate_left(self, node: Node) -> Node:
        reversed_node = node.right
        node.right = reversed_node.left
        reversed_node.left = node

        node.right_childs_count = ((1 if node.right else 0)
                                   + getattr(node.right, "right_childs_count", 0)
                                   + getattr(node.right, "left_childs_count", 0))
        reversed_node.left_childs_count = 1 + node.left_childs_count + node.right_childs_count
        return reversed_node

    def _rotate_right(self, node: Node) -> Node:
        reversed_node = node.left
        node.left = reversed_node.right
        reversed_node.right = node

        node.left_childs_count = ((1 if node.left else 0)
                                  + getattr(node.left, "right_childs_count", 0)
                                  + getattr(node.left, "left_childs_count", 0))
        reversed_node.right_childs_count = 1 + node.left_childs_count + node.right_childs_count
        return reversed_node

    def is_balanced(self, node: Node) -> bool:
        return height(node.left) == height(node.right)

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
        left_height = 0 if not node.left else height(node.left)
        right_height = 0 if not node.right else height(node.right)
        return left_height - right_height

    def _rotations(self, node: Node, diff: int) -> Node:
        if diff == 0:
            return node
        elif diff > 0:
            if self._bfactor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        else:
            if self._bfactor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        return node

    def find_k_element(
        self, node: Node, k: int
    ) -> Union[Optional[Node], Tuple[Optional[Node], List[int]]]:
        element = None
        if node:
            current = node
            while current:
                if current.left_childs_count + 1 == k:
                    element = current
                    current = None
                elif k > current.left_childs_count:
                    k = k - (current.left_childs_count + 1)
                    current = current.right
                else:
                    current = current.left

        return element

    def balance_by_kth_min_element(self, node: Node):
        k = int((node.left_childs_count + node.right_childs_count) / 2) + 1
        kth_element = self.find_k_element(node, k)

        while(node.key != kth_element.key):
            node = self._rotations(node, self._bfactor(node))
        if node.left:
            node.left = self.balance_by_kth_min_element(node.left)
        if node.right:
            node.right = self.balance_by_kth_min_element(node.right)
        return node


def height(node: Node) -> int:
    if not node:
        return 0
    return 1 + max(height(node.right), height(node.left))


def child_count(node: Node) -> int:
    if not node:
        return 0
    return 1 + child_count(node.right) + child_count(node.left)
