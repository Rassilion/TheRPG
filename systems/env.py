from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class Kill(System):
    def update(self, dt):
        # make copy of iterator
        for e, c in tuple(self.entity_manager.pairs_for_type(Health)):
            if c.hp <= 0:
                # create item
                # TODO add some template for droped items
                wep1 = self.entity_manager.create_entity()
                self.entity_manager.add_component(wep1, Item())
                self.entity_manager.add_component(wep1, Weapon())
                self.entity_manager.add_component(wep1, Str(10))
                self.entity_manager.add_component(wep1, Visible())
                pos = self.entity_manager.component_for_entity(e, Position)
                self.entity_manager.add_component(wep1, Position(pos.x, pos.y))
                self.entity_manager.add_component(wep1, Name("Basic Sword 2"))
                # remove dead
                self.entity_manager.remove_entity(e)


class SpawnMob(System):
    """System for spawning random mobs"""

    # TODO add some template for random mobs
    def update(self, dt):
        e = self.entity_manager.pairs_for_type(AI)
        if sum(1 for _, __ in e) <= 10:
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
            eman.add_component(mob1, Vision(5))
