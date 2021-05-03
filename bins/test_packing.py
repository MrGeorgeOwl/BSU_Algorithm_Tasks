from typing import List
from math import ceil

import pytest

from packings import best_fit, first_fit, next_fit, first_fit_decreasing


@pytest.mark.parametrize("algo", [
    next_fit,
    first_fit,
    best_fit,
    first_fit_decreasing,
])
def test_nf(algo):
    weights = [2, 5, 4, 7, 1, 3, 8]
    bin_weight = 10
    amount_of_bins = algo(bin_weight, weights)
    assert amount_of_bins >= min_amount_bins(bin_weight, weights)


def min_amount_bins(bin_weight: int, weights: List[int]) -> int:
    return ceil(sum(weights) / bin_weight)
