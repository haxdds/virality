from PopulationEngine import *


class Community:

    def __init__(self, populations, open_borders=True):
        self.populations = []
        self.populations.extend(populations)

        self.open_borders = open_borders


