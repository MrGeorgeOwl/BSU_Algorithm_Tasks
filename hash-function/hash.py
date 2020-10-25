from typing import Any, Callable, Optional

from resolvers import CollisionResolver

A = 0.31506

def hash(table_size: int, key: int) -> int:
    """
    Hash function which uses multiplication method.
    """
    return int(table_size * (key * A % 1)) 


class Node:
    def __init__(self, value: Any, key: int):
        self.value = value
        self.key = key 
        self.next = None


class HashTable:

    def __init__(self, hash_function: Callable[[int, int], int]):
        self.array = [None for _ in range(50)]
        self.hash_function = hash_function
        self.collision_resolver = CollisionResolver()

    def add_key(self, key: int, value: Any) -> int:
        index = self.hash_function(key, len(self.array))
        if not self.array[index]:
            self.array[index] = Node(value, key)
        else:
            # if resolver is not resetted it will raise Exception
            self.collision_resolver.resolve_collision(self, index, key)
    
    def get_value_of_key(self, key: int) -> Any:
        index = self.hash_function(key, len(self.array))
        if (place := self.array[index]):
            if (place.key != key):
                place = self.collision_resolver.find_node(self, index, key)
            return place.value
        raise Exception(f"No value with key: {key}")        

