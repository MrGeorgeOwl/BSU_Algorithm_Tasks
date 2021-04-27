from typing import List
from math import ceil

import pytest

from packings import next_fit, first_fit


@pytest.mark.parametrize("algo", [
    next_fit,
    first_fit,
])
def test_nf(algo):
    weights = [2, 5, 4, 7, 1, 3, 8]
    bin_weight = 10
    assert algo(bin_weight, weights) >= min_amount_bins(bin_weight, weights)


def min_amount_bins(bin_weight: int, weights: List[int]) -> int:
    return ceil(sum(weights) / bin_weight)
