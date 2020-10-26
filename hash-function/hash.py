import pdb
from typing import Any, Callable, Optional

from resolvers import CollisionResolver
from node import Node

class HashTable:

    def __init__(self, hash_function: Callable[[int, int], int]):
        self.array = [None for _ in range(50)]
        self.hash_function = hash_function
        self.collision_resolver = CollisionResolver()

    def add_key(self, key: int, value: Any) -> int:
        index = self.hash_function(len(self.array), key)
#        pdb.set_trace()
        if not self.array[index]:
            self.array[index] = Node(value, key)
        else:
            # if resolver is not resetted it will raise Exception
            self.collision_resolver.resolve_collision(self, index, value, key)
    
    def get_value_of_key(self, key: int) -> Any:
        index = self.hash_function(len(self.array), key)
        if (place := self.array[index]):
            if (place.key != key):
                place = self.collision_resolver.find_node(self, index, key)
            return place.value
        raise Exception(f"No value with key: {key}")        

