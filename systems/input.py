from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *
from systems import Display


class Input(System):
    """Input system to parse player inputs"""

    def update(self, dt):
        player, pla = next(self.entity_manager.pairs_for_type(Player))
        pos = self.entity_manager.component_for_entity(player, Position)
        phealt = self.entity_manager.component_for_entity(player, Health)
        s = str(pos.pos) + "|" + str(phealt.hp) + "/" + str(phealt.max_hp) + "> "
        input = raw_input(s)
        input = input.split()
        try:
            # wait command
            if input[0] == "wait":
                pass
            if input[0] == "cd":
                self.system_manager.remove_system(Display)
            if input[0] == "od":
                self.system_manager.add_system(Display())
            # move command
            if input[0] == "move":
                if input[1] == "left":
                    pos.x -= 1
                if input[1] == "right":
                    pos.x += 1
                if input[1] == "up":
                    pos.y += 1
                if input[1] == "down":
                    pos.y -= 1
            # list visible entities in vision range
            if input[0] == "look":
                # get vision range
                range = self.entity_manager.component_for_entity(player, Vision).value
                for e, v in self.entity_manager.pairs_for_type(Visible):
                    e_position = self.entity_manager.component_for_entity(e, Position)
                    if e_position.distance(pos) <= range:
                        print self.entity_manager.component_for_entity(e, Name).name + " " + str(e_position.pos)
            # list items in vision range and ask for take
            if input[0] == "take":
                # get vision range
                range = self.entity_manager.component_for_entity(player, Vision).value
                i = 1
                list = []
                # get entities contain Item component
                for e, v in self.entity_manager.pairs_for_type(Item):
                    try:
                        # check if item has position
                        e_position = self.entity_manager.component_for_entity(e, Position)
                        if e_position.distance(pos) <= range and self.entity_manager.component_for_entity(e, Visible):
                            # list items
                            list.append(e)
                            print str(i) + ") " + self.entity_manager.component_for_entity(e, Name).name
                            i += 1
                    except NonexistentComponentTypeForEntity:
                        continue
                # prompt player for item take
                if len(list) == 0:
                    print "No items near"
                else:
                    print "0) Take all"
                    # TODO error handling
                    choice = raw_input("Choice: ")
                    # add item to inventory
                    if choice == "0":
                        for e in list:
                            # add all items to inventory
                            self.entity_manager.add_component(e, Inventory())
                    else:
                        # add choice to inventory
                        self.entity_manager.add_component(list[int(choice) - 1], Inventory())
            if input[0] == "inv":
                # list inventory items
                # TODO prompt player for equip, drop...
                i = 1
                list = []
                for e, v in self.entity_manager.pairs_for_type(Inventory):
                    list.append(e)
                    print str(i) + ") " + self.entity_manager.component_for_entity(e, Name).name
                    i += 1

        except IndexError:
            pass
