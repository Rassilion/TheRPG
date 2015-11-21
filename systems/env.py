from random import randint

from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class Kill(System):
    def update(self, dt):
        # make copy of iterator
        for e, c in tuple(self.entity_manager.pairs_for_type(Health)):
            if c.hp <= 0:
                self.entity_manager.remove_entity(e)


class SpawnMob(System):
    def update(self, dt):
        eman = self.entity_manager
        mob1 = eman.create_entity()
        eman.add_component(mob1, Position(x=randint(0, 100), y=randint(0, 100)))
        eman.add_component(mob1, Velocity(randint(-1, 1), randint(-1, 1)))
        eman.add_component(mob1, AI())
        eman.add_component(mob1, Name("Mob" + str(mob1._guid)))
        eman.add_component(mob1, Health(100))
        eman.add_component(mob1, Str(randint(0, 20)))
        eman.add_component(mob1, Def(randint(0, 20)))
        eman.add_component(mob1, Visible())
