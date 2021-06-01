import random
from dataclasses import dataclass
from typing import List, Tuple, Optional

from numpy import mean

BORDER = 100
POPULATION_AMOUNT = 1000
RESULT = -50
SELECTION_SIZE = round(0.6 * POPULATION_AMOUNT)
RANDOM_SUBSET_SIZE = POPULATION_AMOUNT
MUTATION_PROBABILITY = 10
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
                (random.randint(-50, 50) if random.random() * 100 > MUTATION_PROBABILITY
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


def f(individual: Individual):
    u, w, x, y, z = individual.get_params()
    return (
            u ** 2 * w ** 2 * x ** 2 * y * z ** 2
            + z
            + u ** 2 * w * y * z
            + u * w * y * z ** 2
            + x * y
    )


def fitness(individual: Individual):
    return abs(RESULT - f(individual))


def tournament_selection(population: List[Individual]):
    random_subset = random.sample(population, RANDOM_SUBSET_SIZE)
    return sorted(random_subset, key=fitness)[:SELECTION_SIZE]


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


def mutation(population: List[Individual]):
    for child in list(reversed(list(sorted(population, key=fitness))))[:CHILD_TO_MUTATE]:
        child.mutate()


def substitution(new_children: List[Individual]) -> List[Individual]:
    return list(sorted(new_children, key=fitness))[:POPULATION_AMOUNT]


def genetic():
    population = [Individual() for _ in range(POPULATION_AMOUNT)]
    while True:
        children = make_crossover(
            tournament_selection(population),
        )
        mutation(children)
        population = substitution(children)
        target_assessments = sorted([fitness(parent) for parent in population])
        print(f'min - {target_assessments[0]}; avg - {mean(target_assessments)}')
        if target_assessments[0] == 0:
            break
    print(sorted(population, key=fitness)[0].get_params())


if __name__ == '__main__':
    genetic()
