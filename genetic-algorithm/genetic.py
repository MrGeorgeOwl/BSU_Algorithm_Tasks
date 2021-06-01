import random
from numpy import mean

BORDER = 100
POPULATION_AMOUNT = 1000
RESULT = 13
SELECTION_SIZE = round(0.6 * POPULATION_AMOUNT)
RANDOM_SUBSET_SIZE = POPULATION_AMOUNT
MUTATION_PROBABILITY = 10
CHILD_TO_MUTATE = round(SELECTION_SIZE / 4)


def f(u, w, x, y, z):
    return w * y + z + u ** 2 * x ** 2 * y * z ** 2 + u * w * x ** 2 * y ** 2 * z ** 2 + w * x * y ** 2 * z ** 2


def target_assessment(args):
    return abs(RESULT - f(*args))


def tournament_selection(population):
    random_subset = random.sample(population, RANDOM_SUBSET_SIZE)
    return sorted(random_subset, key=target_assessment)[:SELECTION_SIZE]


def count_probability(first_child, second_child):
    first_elem_probability = target_assessment(second_child) / (target_assessment(first_child) + target_assessment(
        second_child))
    return [first_elem_probability, 1 - first_elem_probability]


def proportional_crossover(first_child, second_child):
    return tuple([random.choices(elem, count_probability(first_child, second_child))[0] for elem in
                  zip(first_child, second_child)])


def make_crossover(population):
    return [proportional_crossover(first_child, population[index + 1]) for index, first_child in
            list(enumerate(population[:-1]))]


def mutation(population):
    for index, child in list(reversed(list(enumerate(sorted(population, key=target_assessment)))))[:CHILD_TO_MUTATE]:
        population[index] = tuple(
            [num if MUTATION_PROBABILITY <= random.randint(1, 100) else random.randint(-50, 50) for num in child])
    return population


def substitution(population, new_children):
    population.sort(key=target_assessment, reverse=True)
    new_children.sort(key=target_assessment, reverse=True)
    for index, parent, child in zip(range(len(population) - 1, -1, -1), population, new_children):
        population[index] = random.choices((parent, child), count_probability(parent, child))[0]
    return population


def genetic():
    population = [tuple(random.sample(range(-BORDER, BORDER), 5)) for _ in range(POPULATION_AMOUNT)]
    target_assessments = [10, ]
    while target_assessments[0] != 0:
        population = substitution(population, mutation(make_crossover(tournament_selection(population))))
        target_assessments = sorted([target_assessment(parent) for parent in population])
        print(f'min - {target_assessments[0]}; avg - {mean(target_assessments)}')
    print(sorted(population, key=target_assessment)[0])


if __name__ == '__main__':
    random.seed(100)
    genetic()
