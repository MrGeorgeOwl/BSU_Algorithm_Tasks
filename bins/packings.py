from random import randint
from typing import List, Tuple

def next_fit(bin_weight: int, element_weights: List[int]) -> int:
    current_bin_weight: int = bin_weight
    amount_of_required_bins: int = 1
    for weight in element_weights:
        if current_bin_weight >= weight:
            current_bin_weight -= weight
        else:
            current_bin_weight = bin_weight
            amount_of_required_bins += 1
    return amount_of_required_bins


def first_fit(bin_weight: int, element_weights: List[int]) -> int:
    bins: List[int] = [bin_weight]
    amount_of_required_bins = 1
    for weight in element_weights:
        for index, space in enumerate(bins):
            if space >= weight:
                bins[index] -= weight
                break
            if index == len(bins) - 1:
                bins.append(bin_weight - weight)
                amount_of_required_bins += 1
                break
    return amount_of_required_bins


def best_fit(bin_weight: int, element_weights: List[int]) -> int:
    amount_of_required_bins = 1
    bins: List[int] = [bin_weight]
    starting_min = bin_weight + 1
    for weight in element_weights:
        bin_index = 0
        current_min = starting_min
        for index, space in enumerate(bins):
            if space <= current_min and space >= weight:
                bin_index = index
                current_min = space

        if current_min == starting_min:
            bins.append(bin_weight)
            amount_of_required_bins += 1
        else:
            bins[bin_index] -= weight
    return amount_of_required_bins


def first_fit_decreasing(bin_weight: int, element_weights: List[int]) -> int:
    reversed_weights = element_weights[:]
    reversed(reversed_weights)
    return first_fit(bin_weight, reversed_weights)


if __name__ == "__main__":
    weights = [randint(1, 10) for _ in range(10_000)]
    bin_weight = 10
    for algo in (next_fit, first_fit, best_fit, first_fit_decreasing):
        print(f"Amount of required bins {algo(bin_weight, weights)} for algo: {algo.__name__}")
