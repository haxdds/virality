import random
import math


class PopulationEngine:

    def __init__(self, population):
        self.population = population

    def random_compute_next(self):
        for person in self.population:

            if not person.is_mobile:
                continue

            x = person.x
            y = person.y
            speed = person.speed

            rand_x_dist = round(random.uniform(0, 1), 2)
            rand_y_dist = round(random.uniform(0, 1), 2)

            rand_x_direction = random.choice([-1, 1])
            rand_y_direction = random.choice([-1, 1])

            normalization_factor = math.sqrt(rand_x_dist ** 2 + rand_y_dist ** 2)

            delta_x = speed * rand_x_dist * rand_x_direction / normalization_factor
            delta_y = speed * rand_y_dist * rand_y_direction / normalization_factor

            new_x = x + delta_x
            new_y = y + delta_y

            person.set_position(new_x, new_y)
