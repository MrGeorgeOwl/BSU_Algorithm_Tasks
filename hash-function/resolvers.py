from node import Node
from hash_functions import double_hash

class CollisionResolver:

    def resolve_collision(self, table, index, value, key):
        raise Exception(f"Already occupied index: {index}")    

    def find_node(self, table, index, key):
        raise Exception(f"No value with key: {key}") 


class ChainCollisionResolver(CollisionResolver):

    def resolve_collision(self, table, index, value, key):
        node = table.array[index]
        node.next = Node(value, key)
        return node.next

    def find_node(self, table, index, key):
        current = table.array[index] 
        while current is not None and current.key != key:
            current = current.next
        if current:
            return current
        raise Exception(f"No such node with key: {key}")


class LinearCollisionResolver(CollisionResolver):
    
    def resolve_collision(self, table, index, value, key):
    # TODO: change algorithm
        possible_indexes = list(
            filter(
                lambda x: table.array[x] is None and x > index,
                range(len(table.array)),
            ),
        )
        new_index = possible_indexes[0]
        table.array[new_index] = Node(value, key)
        return table.array[new_index] 
    
    def find_node(self, table, index, key):
    # TODO: change algorithm
        possible_indexes = list(
            filter(
                lambda x: table.array[x] is not None and x > index,
                range(len(table.array)),
            ),
        ) 
        possible_indexes = list(
            filter(
                lambda x: table.array[x].key == key,
                possible_indexes,
            ),
        )
        if possible_indexes:
            return table.array[possible_indexes[0]]
        raise Exception(f"No such node with key: {key}")


class DoubleHashingCollisionResolver(CollisionResolver):
    
    def resolve_collision(self, table, index, value, key):
        counter = 1
        new_index = double_hash(len(table.array), key)
        first_new_index = new_index
        while table.array[new_index]:
            if first_new_index == new_index:
                raise Exception(f"No room for key: {key}")
            counter += 1
            new_index = double_hash(len(table.array), key, counter)
        table.array[new_index] = Node(value, key)
        return table.array[new_index]
    
    def find_node(self, table, index, key):
        first_double_hashed_index = double_hash(len(table.array), key)
        if table.array[first_double_hashed_index].key != key:
            counter = 2
            current_index = double_hash(len(table.array), key, counter)
            while current_index != first_double_hashed_index:
                current_node = table.array[current_index]
                if current_node and current_node.key == key:
                    return current_node
                else:
                    counter += 1
                    current_index = double_hash(len(table.array), key, counter)
            raise Exception(f"No such node with key: {key}")
        return table.array[first_double_hashed_index]
