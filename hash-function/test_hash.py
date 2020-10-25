import pdb
import pytest

from hash import hash, HashTable

@pytest.mark.parametrize("key, table_size, exp", [
    (1, 50, 15),
    (2, 50, 31),
    (30, 50, 22),    
])
def test_hash(key, table_size, exp):
    assert hash(table_size, key) == exp


def test_table_add_key():
    table = HashTable(hash)
    table.add_key(0, "value")
    assert table.get_value_of_key(0) == "value"


def test_table_add_key_to_same_place():
    table = HashTable(hash)
    table.add_key(0, "value")
    with pytest.raises(Exception):
        table.add_key(0, "another value")


def test_table_get_value_while_no_key():
    table = HashTable(hash)
    with pytest.raises(Exception):
        table.get_value_of_key(0)


def test_chaining_resolver(table_with_chain_resolver):
    table_with_chain_resolver.add_key(5, "first_chain")
    table_with_chain_resolver.add_key(24, "second_chain")
    assert table_with_chain_resolver.get_value_of_key(5) == "first_chain"
    assert table_with_chain_resolver.get_value_of_key(24) == "second_chain"


def test_linear_resolver(table_with_linear_resolver):
    table_with_linear_resolver.add_key(5, "first")
    table_with_linear_resolver.add_key(24, "second")
    assert table_with_linear_resolver.get_value_of_key(5) == 'first'
    assert table_with_linear_resolver.get_value_of_key(24) == 'second'

