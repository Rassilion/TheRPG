from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class Input(System):
    """Input system to parse player inputs"""
    def update(self, dt):
        player, pla = next(self.entity_manager.pairs_for_type(Player))
        phealt = self.entity_manager.component_for_entity(player, Health)
        s = str(phealt.hp) + "/" + str(phealt.max_hp) + "> "
        input = raw_input(s)
        input = input.split()
        try:
            if input[0] == "wait":
                pass
            if input[0] == "move":
                pos = self.entity_manager.component_for_entity(player, Position)
                vel = self.entity_manager.component_for_entity(player, Velocity)
                if input[1] == "left":
                    pos.x -= 1
                if input[1] == "right":
                    pos.x += 1
                if input[1] == "up":
                    pos.y += 1
                if input[1] == "down":
                    pos.y -= 1
            if input[0] == "look":
                pass
        except IndexError:
            pass
