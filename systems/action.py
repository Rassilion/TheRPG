from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *
from systems import getvalueor0


class Movement(System):
    """Movement system to update position of Velocity components."""

    def update(self, dt):
        # get entities contain Velocity component
        for e, vel in self.entity_manager.pairs_for_type(Velocity):
            try:
                # check if they have Position
                pos = self.entity_manager.component_for_entity(e, Position)
            except NonexistentComponentTypeForEntity:
                print("%s has a Velocity but no Position component, cannot move it.", e)
                continue
            # increase position by velocity
            pos.x += vel.dx * dt
            pos.y += vel.dy * dt


class Attack(System):
    """collided mobs and player attack each other"""

    def update(self, dt):
        # get entities contain AI component
        for e, ai in self.entity_manager.pairs_for_type(AI):
            try:
                # get player
                player, pla = next(self.entity_manager.pairs_for_type(Player))
                # get positions
                ppos = self.entity_manager.component_for_entity(player, Position)
                pos = self.entity_manager.component_for_entity(e, Position)
            except NonexistentComponentTypeForEntity:
                continue
            if pos.collision(ppos):
                # TODO cleaner way to do this
                eman = self.entity_manager
                try:
                    # get AI weapon
                    aiatk = eman.component_for_entity(e, Equip).getstr(eman)
                except NonexistentComponentTypeForEntity:
                    aiatk = 0
                # calc damage "dmg=str-target def"
                # player hp - monsters atk
                eman.component_for_entity(player,
                                          Health).decreasehealt(
                        aiatk + getvalueor0(eman, e, Str) - getvalueor0(eman, player, Def))

                try:
                    # get player weapon
                    patk = eman.component_for_entity(player, Equip).getstr(eman)
                except NonexistentComponentTypeForEntity:
                    patk = 0
                eman.component_for_entity(e,
                                          Health).decreasehealt(
                        patk + getvalueor0(eman, player, Str) - getvalueor0(eman, e, Def))
