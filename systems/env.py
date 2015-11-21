from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class Kill(System):
    def update(self, dt):
        # make copy of iterator
        for e, c in tuple(self.entity_manager.pairs_for_type(Health)):
            if c.hp <= 0:
                self.entity_manager.remove_entity(e)
