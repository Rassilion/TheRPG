from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class Display(System):
    def update(self, dt):
        for e, c in self.entity_manager.pairs_for_type(Position):
            try:
                name = self.entity_manager.component_for_entity(e, Name)
                hp = self.entity_manager.component_for_entity(e, Health).hp
            except NonexistentComponentTypeForEntity:
                print("%s has no name.", e)
                name = e

            print("{} position, hp {}: {!r}".format(name.name, hp, c.pos))
