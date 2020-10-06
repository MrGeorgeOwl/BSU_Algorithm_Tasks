import pytest

from search import binary_search, interpolation_search


@pytest.mark.parametrize("number, array, expected", [
    (4, [1, 2, 3, 4, 5], 3),
    (6, [1, 2, 3, 4, 5], -1),
    (33, [i for i in range(1, 101)], 32),
    (101, [i for i in range(1, 101)], -1),
])
def test_binary_search(number, array, expected):
    actual = binary_search(number, array)
    assert actual == expected


def test_binary_search_exception():
    with pytest.raises(Exception):
        binary_search(1, [])


@pytest.mark.parametrize("number, array, expected", [
    (4, [1, 2, 3, 4, 5], 3),
    (6, [1, 2, 3, 4, 5], -1),
    (33, [i for i in range(1, 101)], 32),
    (101, [i for i in range(1, 101)], -1),
])
def test_interpolation_search(number, array, expected):
    actual = interpolation_search(number, array)
    assert actual == expected


def test_interpolation_search_exception():
    with pytest.raises(Exception):
        interpolation_search(1, [])

