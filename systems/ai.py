from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *
from systems import getvalueor0


class AIMove(System):
    """update velocity of ai entities to player direction"""

    def update(self, dt):
        player, pla = next(self.entity_manager.pairs_for_type(Player))
        # get positions
        ppos = self.entity_manager.component_for_entity(player, Position)
        for e, ai in self.entity_manager.pairs_for_type(AI):
            epos = self.entity_manager.component_for_entity(e, Position)
            range = self.entity_manager.component_for_entity(e, Vision).value
            # check vision range
            if epos.distance(ppos) <= range:
                # get velocity
                vel = self.entity_manager.component_for_entity(e, Velocity)
                try:
                    vel.dx = (ppos.x - epos.x) / abs(ppos.x - epos.x)
                except ZeroDivisionError:
                    vel.dx = 0
                try:
                    vel.dy = (ppos.y - epos.y) / abs(ppos.y - epos.y)
                except ZeroDivisionError:
                    vel.dy = 0
            else:
                # TODO patrolling movement
                pass
