from CommunityEngine import *


class WorldEngine:

    def __init__(self, world):
        self.world = world

        self.community_engines = {}
        for community in self.world.communities:
            self.community_engines[community] = CommunityEngine(community)

    def random_compute_next(self):
        for community, engine in self.community_engines.items():
            engine.random_compute_next()



