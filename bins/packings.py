from typing import List, Tuple

def next_fit(bin_weight: int, element_weights: List[int]) -> int:
    bins: List[List[int]] = [[]]
    current_bin_weight: int = bin_weight
    amount_of_required_bins: int = 1
    for weight in element_weights:
        if current_bin_weight >= weight:
            bins[-1].append(weight)
            current_bin_weight -= weight
        else:
            current_bin_weight = bin_weight
            bins.append([])
            amount_of_required_bins += 1
    return amount_of_required_bins


def first_fit(bin_weight: int, element_weights: List[int]) -> int:
    bins: List[List[int, List[int]]] = [[bin_weight, []]]
    amount_of_required_bins = 1
    for weight in element_weights:
        is_added = False
        for index, (space, weights) in enumerate(bins):
            if space >= weight:
                weights.append(weight)
                bins[index][0] -= weight
                is_added = True
            if is_added:
                break
        if not is_added:
            bins.append([bin_weight - weight, [weight]])
            amount_of_required_bins += 1
    return amount_of_required_bins
