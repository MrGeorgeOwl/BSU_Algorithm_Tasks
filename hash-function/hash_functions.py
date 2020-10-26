
A = 0.31506

def hash(table_size: int, key: int, a: int = A) -> int:
    """
    Hash function which uses multiplication method.
    """
    return int(table_size * (key * a % 1)) 


def hash_division_method(table_size: int, key: int) -> int:
    """
    Hash function which uses division method.
    """
    return key % table_size


def double_hash(table_size: int, key: int, multiplier: int = 1) -> int:
    return (hash(table_size, key) 
            + multiplier * hash_division_method(table_size, key)
           ) % table_size

