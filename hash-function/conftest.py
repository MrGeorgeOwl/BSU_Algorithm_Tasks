import pytest

from hash import hash, HashTable, Node
from resolvers import ChainCollisionResolver, LinearCollisionResolver

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

