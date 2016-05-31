
from random import randrange

def mean_fitness_selection(population, crossover, fitness):

    mean_fitness = get_mean_fitness(population, fitness)

    new_population = [image_gem for image_gen in population if fitness(image_gen) >= mean_fitness]

    best_part = len(new_population)

    while len(new_population) < len(population):
        parent_1 = new_population[randrange(best_part)]
        parent_2 = new_population[randrange(best_part)[

        new_population.append(crossover(parent_1, parent_2))

    return new_population

def get_mean_fitness(population, fitness):

    f = 0.0

    for image_gen in population:
        f += fitness(image_gen)

    return f / len(population)
