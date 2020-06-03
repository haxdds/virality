import Person
import random
import numpy as np

class PersonFactory:

    def random(id):
        age = PersonFactory.__random_age()
        health = random.uniform(0.5, 1)



    def __random_age(mean_age=38, std_age=13):
        randomNum = np.random.normal(loc=mean_age, scale=std_age, size=1)
        rand = np.round(randomNum)
        age = 0 if rand < 0 else 100 if rand > 100 else rand
        return age


print(PersonFactory().__random_age())