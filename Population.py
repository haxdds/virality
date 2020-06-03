import random
import math
from Person import *


class Population:

    def __init__(self, population=None, size=None):
        self.population = []
        if population is not None:
            self.population = population
        else:
            for i in range(size):
                age = random.randint(1, 100)
                health = random.uniform(0, 1)
                new_person = Person(i, age=age, health=health)
                self.population.append(new_person)


