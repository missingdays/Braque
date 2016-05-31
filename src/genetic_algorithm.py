
from image_gen import *
from selection import *
from crossover import *
from mutation import *
from fitness_function import *

class GeneticAlgorithm:

    def __init__(self, cycle_number=100, population_size=50, 
            selection, crossover=binary_crossover, mutation=independent_mutation, fitness_function=None):

        self.cycle_number = cycle_number
        self.population_size = population_size
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.fitness_function = fitness_function

        self.original_image = None
        self.population = []

    def set_original_image(self, original_image):
        self.original_image = original_image

    def __iter__(self):

        self.begin_evolution()

        return self

    def __next__(self):
        return self.next()

    def next(self):

        self.cycle()

        if self.current_cycle > self.cycle_number:
            raise StopIteration()

        return self.population

    def begin_evolution(self):

        if self.original_image == None:
            raise Exception("Set original image before performing evolution")

        self.generate_first_population()

    def generate_first_population(self):

        self.population = []

        for i in range(self.population_size):
            self.population.append(ImageGen.random())

    def cycle(self):

        new_population = self.selection(self.population, self.crossover, self.fitness_function)

        self.mutation(new_population)

        self.population = new_population
