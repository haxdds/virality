import random


class Person:

    def __init__(self, id, age=25, health=1, x=0, y=0, is_mobile=True, speed=1, size=1):
        self.id = id
        self.age = age
        self.health = health
        self.x = x
        self.y = y
        self.is_mobile = is_mobile
        self.speed = speed
        self.size = size

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_health(self, health):
        self.health = health
