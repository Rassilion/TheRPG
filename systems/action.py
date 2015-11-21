from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *
from systems import getvalueor0


class Movement(System):
    """Movement system to update position of Movable components."""

    def update(self, dt):
        for e, vel in self.entity_manager.pairs_for_type(Velocity):
            try:
                pos = self.entity_manager.component_for_entity(e, Position)
            except NonexistentComponentTypeForEntity:
                print("%s has a Velocity but no Position component, cannot move it.", e)
                continue
            pos.x += vel.dx * dt
            pos.y += vel.dy * dt


class Attack(System):
    """collided entities attack each other"""

    def update(self, dt):
        for e, ai in self.entity_manager.pairs_for_type(AI):
            try:
                player, pla = next(self.entity_manager.pairs_for_type(Player))
                ppos = self.entity_manager.component_for_entity(player, Position)
                pos = self.entity_manager.component_for_entity(e, Position)
            except NonexistentComponentTypeForEntity:
                continue
            if pos.collision(ppos):
                # TODO cleaner way to do this
                eman = self.entity_manager
                try:
                    aiwep = eman.component_for_entity(e, Equip).weapon
                    aiatk = eman.component_for_entity(aiwep, Str).value
                except NonexistentComponentTypeForEntity:
                    aiatk = 0
                eman.component_for_entity(player,
                                          Health).hp -= aiatk + getvalueor0(eman, e, Str) - getvalueor0(
                    eman, player, Def)
                try:
                    pwep = eman.component_for_entity(player, Equip).weapon
                    patk = eman.component_for_entity(pwep, Str).value
                except NonexistentComponentTypeForEntity:
                    patk = 0
                eman.component_for_entity(e,
                                          Health).hp -= patk + getvalueor0(eman, player,
                                                                           Str) - getvalueor0(eman, e,
                                                                                              Def)
