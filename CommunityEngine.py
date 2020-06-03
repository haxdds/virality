from PopulationEngine import *


class CommunityEngine:

    def __init__(self, community):
        self.community = community
        self.population_engines = {}
        for population in self.community.populations:
            self.population_engines[population] = PopulationEngine(population)

    def random_compute_next(self):
        for population, engine in self.population_engines.items():
            engine.random_compute_next()