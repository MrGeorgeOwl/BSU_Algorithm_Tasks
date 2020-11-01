from typing import Dict, List
import random
import sys

from hash_functions import A, hash


KNUT_NUMBER = 0.618033


def experiment(sets_amount: int, keys_amount: int, number_range: int, table_size: int):
    sets = _generate_sets(sets_amount, keys_amount, number_range)
    length_lists_in_sets = []

    _fill_array_with_lists_length(length_lists_in_sets, sets, table_size, KNUT_NUMBER)
    max_length = max(length_lists_in_sets)
    print(f"Max length of lists while hashing with A={KNUT_NUMBER}: {max_length}")
    
    length_lists_in_sets.clear()
    _fill_array_with_lists_length(length_lists_in_sets, sets, table_size, A)
    max_length = max(length_lists_in_sets)
    print(f"Max length of lists while hashing with A={A}: {max_length}")


def _generate_sets(sets_amount: int, keys_amount: int, number_range: int) -> List[List[int]]:
    return [[random.randint(1, number_range) for _ in range(keys_amount)] 
            for _ in range(sets_amount)]


def _fill_array_with_lists_length(length_lists_in_sets: List[int], sets: List[List[int]], table_size: int, A: float) -> None:
    for set in sets:
        indexes_keys = _hash_keys_of_set(set, table_size, A)
        max_length = max([len(items) for key, items in indexes_keys.items()])
        length_lists_in_sets.append(max_length)


def _hash_keys_of_set(set: List[int], table_size: int, A: float) -> Dict:
    indexes_keys = {}
    for key in set:
        index = hash(table_size, key, A)
        if index not in indexes_keys.keys():
            indexes_keys[index] = []
        indexes_keys[index].append(key)
    return indexes_keys
    

if __name__ == '__main__':
    p, n, r, m = list(map(lambda x: int(x), sys.argv[1:]))
    experiment(p, n, r, m)

