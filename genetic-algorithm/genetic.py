import random
from dataclasses import dataclass
from typing import List, Tuple, Optional, Callable

from numpy import mean

BORDER = 100
POPULATION_AMOUNT = 1000
RESULT = 22
SELECTION_SIZE = round(0.6 * POPULATION_AMOUNT)
RANDOM_SUBSET_SIZE = POPULATION_AMOUNT
MUTATION_PROBABILITY = 40
CHILD_TO_MUTATE = round(SELECTION_SIZE / 4)


@dataclass
class Individual:
    u: int
    w: int
    x: int
    y: int
    z: int

    def __init__(
            self,
            u: Optional[int] = None,
            w: Optional[int] = None,
            x: Optional[int] = None,
            y: Optional[int] = None,
            z: Optional[int] = None,
    ):
        self.u = u or random.randint(-BORDER, BORDER)
        self.w = w or random.randint(-BORDER, BORDER)
        self.x = x or random.randint(-BORDER, BORDER)
        self.y = y or random.randint(-BORDER, BORDER)
        self.z = z or random.randint(-BORDER, BORDER)

    def get_params(self):
        return self.u, self.w, self.x, self.y, self.z

    def mutate(self):
        for attr in ("u", "w", "x", "y", "z"):
            setattr(
                self,
                attr,
                (random.randint(-BORDER, BORDER) if random.random() * 100 > MUTATION_PROBABILITY
                 else getattr(self, attr)),
            )


def multipoint_crossover(
        first_parent: Individual,
        second_parent: Individual,
) -> Tuple[Individual, Individual]:
    first_params = first_parent.get_params()
    second_params = second_parent.get_params()
    return (
        Individual(*(first_params[:2] + second_params[2:4] + first_params[4:])),
        Individual(*(second_params[:2] + first_params[2:4] + second_params[4:])),
    )


def onepoint_crossover(
        first_parent: Individual,
        second_parent: Individual,
) -> Tuple[Individual, Individual]:
    first_params = first_parent.get_params()
    second_params = second_parent.get_params()
    return (
        Individual(*(first_params[:3] + second_params[3:])),
        Individual(*(second_params[:3] + first_params[3:]))
    )


def f1(individual: Individual):
    u, w, x, y, z = individual.get_params()
    return (
            u ** 2 * w ** 2 * x ** 2 * y * z ** 2
            + z
            + u ** 2 * w * y * z
            + u * w * y * z ** 2
            + x * y
    )


def f2(individual: Individual):
    u, w, x, y, z = individual.get_params()
    return (
        w**2 * x * y**2
        + u**2 * x**2 * y**2
        + u * w**2 * x * y
        + x**2 * z**2
        + z
    )


def f3(individual: Individual):
    u, w, x, y, z = individual.get_params()
    return (
        w**2 * z
        + u * z**2
        + y**2
        + u * w * x**2 * y**2 * z**2
        + w * y * z
    )


def fitness(individual: Individual, target: Callable):
    return abs(RESULT - target(individual))


def tournament_selection(population: List[Individual], target: Callable):
    random_subset = random.sample(population, RANDOM_SUBSET_SIZE)
    return sorted(random_subset, key=lambda x: fitness(x, target))[:SELECTION_SIZE]


def make_crossover(
        population: List[Individual],
) -> List[Individual]:
    amount_of_parents = round(len(population) / 2)
    first_parents = [
        population.pop(random.randint(0, len(population) - 1))
        for _ in range(amount_of_parents)
    ]
    children_pairs_multi = [
        multipoint_crossover(first_parent, second_parent)
        for first_parent, second_parent in zip(first_parents, population)
    ]
    children_pairs_onepoint = [
        onepoint_crossover(first_parent, second_parent)
        for first_parent, second_parent in zip(first_parents, population)
    ]
    children_pairs_onepoint.extend(children_pairs_multi)
    return [
        child for pair in children_pairs_onepoint for child in pair
    ]


def mutation(population: List[Individual], target):
    for child in list(reversed(list(sorted(population, key=lambda x: fitness(x, target)))))[:CHILD_TO_MUTATE]:
        child.mutate()


def substitution(new_children: List[Individual], target) -> List[Individual]:
    return list(sorted(new_children, key=lambda x: fitness(x, target)))[:POPULATION_AMOUNT]


def genetic(target):
    population = [Individual() for _ in range(POPULATION_AMOUNT)]
    generation = 1
    while True:
        children = make_crossover(
            tournament_selection(population, target),
        )
        mutation(children, target)
        population = substitution(children, target)
        target_assessments = sorted([fitness(child, target) for child in population])
        print(f'min - {target_assessments[0]}; avg - {mean(target_assessments)}; generation - {generation}')
        if target_assessments[0] == 0:
            break
        generation += 1
    print(sorted(population, key=lambda x: fitness(x, target))[0].get_params())


if __name__ == '__main__':
    # print(f"{f1.__name__}")
    # genetic(f1)
    # print(f"{f2.__name__}")
    # genetic(f2)
    print(f"{f3.__name__}")
    genetic(f3)
