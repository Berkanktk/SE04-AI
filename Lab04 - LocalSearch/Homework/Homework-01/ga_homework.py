import random
import queens_fitness

p_mutation = 0.2
num_of_generations = 10


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("\nGeneration {}:".format(generation))
        print_population(population, fitness_fn)
        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        population = population.union(new_population)
        population = filter_population(population, fitness_fn)
        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("\n*******************************************")
    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)
    print("*******************************************")

    return fittest_individual


def filter_population(population, fitness_fn):
    new_population = set()
    for individual in population:
        if fitness_fn(individual) > - 7:
            new_population.add(individual)
    return new_population


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    """
    Reproduce two individuals with single-point crossover
    Return the child individual
    """

    size = len(father)
    child = [0] * size
    i = random.randint(0, size - 1)

    while i < size - 1:
        child[i] = mother[i]
        child[i] = father[i]
        i += 1

    return tuple(child)


def mutate(individual):
    """
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    """

    # print("individual:", individual)
    if len(individual) > 0:
        number = random.randint(0, len(individual) - 1)  # Select random number
        mutated = [0] * len(individual)

        for i in range(0, len(individual)):
            if i != number:
                mutated[i] = individual[i]
            else:
                mutated[i] = random.randint(1, 9)

        # "print("final mut:", mutated)

        return tuple(mutated)


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    fitness_population = []
    stagnate_value = random.randint(0, 100)  # less fit individuals are occasionally selected
    total_fitness = 0
    mother_index = 0

    # Look for all individuals
    for individual in ordered_population:
        total_fitness += fitness_fn(individual)
        # print("individual:", individual)

    # Fit values for the individuals
    for individual in ordered_population:
        fitness_population.append(fitness_fn(individual))
        # print("individual pop:", fitness_population)

    father_index = fitness_population.index(max(fitness_population))
    # print("fittest father at:", father_index)
    fitness_population.remove(max(fitness_population))
    # print("fittest father removed:", fitness_population)

    try:
        if stagnate_value > p_mutation * 100:
            mother_index = fitness_population.index(max(fitness_population))  # Return index of the fittest mother
            # print("stag mother ind:", mother_index)
        else:
            while mother_index != father_index:
                mother_index = random.randint(0, len(ordered_population))
    except:
        print("Max is empty")

    # print("fittest mother", ordered_population[mother_index])
    # print("fittest father:", ordered_population[father_index])

    return ordered_population[mother_index], ordered_population[father_index]


def fitness_function(individual):
    """
    Computes the decimal value of the individual
    Return the fitness level of the individual

    Explanation:
    enumerate(list) returns a list of pairs (position, element):

    enumerate((4, 6, 2, 8)) -> [(0, 4), (1, 6), (2, 2), (3, 8)]

    enumerate(reversed((1, 1, 0))) -> [(0, 0), (1, 1), (2, 1)]
    """
    l = list(individual)
    fitness = int("".join(str(x) for x in l), 2)  # Base 2

    return fitness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    """
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    """
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 0

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (3, 4, 2, 6, 1, 7, 8, 5),
        (4, 6, 4, 2, 7, 3, 5, 4)
    }

    fittest = genetic_algorithm(initial_population, queens_fitness.fitness_fn_negative, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + " fitness: " + str(queens_fitness.fitness_fn_negative(fittest)))


if __name__ == '__main__':
    pass
    main()
