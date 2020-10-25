import pytest

from hash import HashTable, Node
from hash_functions import hash
from resolvers import (
    ChainCollisionResolver,
    DoubleHashingCollisionResolver,
    LinearCollisionResolver,
)

@pytest.fixture(scope='function')
def table_with_chain_resolver():
    table = HashTable(hash)
    table.collision_resolver = ChainCollisionResolver()
    return table


@pytest.fixture(scope='function')
def table_with_linear_resolver():
    table = HashTable(hash)
    table.collision_resolver = LinearCollisionResolver()
    return table


@pytest.fixture(scope='function')
def table_with_double_resolver():
    table = HashTable(hash)
    table.collision_resolver = DoubleHashingCollisionResolver()
    return table

