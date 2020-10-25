class CollisionResolver:

    def resolve_collision(self, table, index, key):
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
        while(current != None or current.key != key):
            current = current.next
        if current:
            return current
        raise Exception(f"No such node with key: {key}")


class LinearCollisionResolver(CollisionResolver):
    
    def resolve_collision(self, table, index, value, key):
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

