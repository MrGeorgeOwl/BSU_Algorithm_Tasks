import random
import sys


def next_fit(bin_weight, element_weights):
    bins = [bin_weight]
    current_bin_index = 0
    amount_of_required_bins = 1
    for weight in element_weights:
        if bins[current_bin_index] > weight:
            bins[current_bin_index] -= weight
        else:
            current_bin_index += 1
            bins.append(bin_weight - weight)
            amount_of_required_bins += 1
    return amount_of_required_bins


def first_fit(bin_weight, element_weights):
    bins = [bin_weight]
    for weight in element_weights:
        for index, space in enumerate(bins):
            if space >= weight:
                bins[index] -= weight
                break
            elif index == len(bins) - 1:
                bins.append(bin_weight - weight)
                break
    return len(bins)


def best_fit(bin_weight, element_weights):
    amount_of_required_bins = 1
    bins = [bin_weight]
    starting_min = sys.maxsize
    for weight in element_weights:
        bin_index = 0
        min_difference = starting_min
        for index, space in enumerate(bins):
            difference = space - weight
            if difference >= 0 and difference < min_difference:
                bin_index = index
                min_difference = difference

        if bins[bin_index] - min_difference < 0:
            bins.append(bin_weight - weight)
            amount_of_required_bins += 1
        else:
            bins[bin_index] -= weight
    return amount_of_required_bins


def first_fit_decreasing(bin_weight, element_weights):
    return first_fit(bin_weight, sorted(element_weights, reverse=True))


if __name__ == "__main__":
    random.seed(100)
    weights = [random.random() for _ in range(10_000)]
    bin_weight = 1
    for algo in (next_fit, first_fit, best_fit, first_fit_decreasing):
        print(f"Amount of required bins {algo(bin_weight, weights)} for algo: {algo.__name__}")
