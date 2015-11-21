from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class Input(System):
    """Input system to parse player inputs"""

    def update(self, dt):
        player, pla = next(self.entity_manager.pairs_for_type(Player))
        pos = self.entity_manager.component_for_entity(player, Position)
        phealt = self.entity_manager.component_for_entity(player, Health)
        s = str(pos.pos)+"|"+str(phealt.hp) + "/" + str(phealt.max_hp) + "> "
        input = raw_input(s)
        input = input.split()
        try:
            if input[0] == "wait":
                pass
            if input[0] == "move":
                if input[1] == "left":
                    pos.x -= 1
                if input[1] == "right":
                    pos.x += 1
                if input[1] == "up":
                    pos.y += 1
                if input[1] == "down":
                    pos.y -= 1
            if input[0] == "look":
                range = self.entity_manager.component_for_entity(player, Vision).value
                for e, v in self.entity_manager.pairs_for_type(Visible):
                    e_position = self.entity_manager.component_for_entity(e, Position)
                    if e_position.distance(pos) <= range:
                        print self.entity_manager.component_for_entity(e, Name).name + " "+str(e_position.pos)
        except IndexError:
            pass
