#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from ecs import EntityManager, SystemManager

from components import *
from systems import *


def parser(eman, player, input):
    input = input.split()
    if input[0] == "move":
        pos = eman.component_for_entity(player, Position)
        vel = eman.component_for_entity(player, Velocity)
        if input[1] == "left":
            pos.x -= vel.dx
        if input[1] == "right":
            pos.x += vel.dx
        if input[1] == "up":
            pos.y += vel.dy
        if input[1] == "down":
            pos.y -= vel.dy
    if input[0] == "look":
        pass


def main():
    # Create an entity manager, a database entities and components.
    database = EntityManager()
    # Create a player entity.
    player = database.create_entity()
    mob1 = database.create_entity()
    mob2 = database.create_entity()
    wep1 = database.create_entity()
    # Add a Movable component instance and its association
    # with the player entity to the database.
    database.add_component(wep1, Weapon(10))
    database.add_component(wep1, Name("Basic Sword"))

    database.add_component(player, Position(x=10, y=10))
    database.add_component(player, Velocity())
    database.add_component(player, Player())
    database.add_component(player, Name("Ra"))
    database.add_component(player, Health(100))
    database.add_component(player, Equip(weapon=wep1))

    database.add_component(mob1, Position(x=15, y=20))
    database.add_component(mob1, Velocity())
    database.add_component(mob1, AI())
    database.add_component(mob1, Name("Mob1"))
    database.add_component(mob1, Health(100))
    database.add_component(mob1, Equip(weapon=wep1))

    database.add_component(mob2, Position(x=11, y=10))
    database.add_component(mob2, AI())
    database.add_component(mob2, Name("Mob2"))
    database.add_component(mob2, Health(100))
    database.add_component(mob2, Equip(weapon=wep1))


    # Create a system manager, i.e. the game world.
    game = SystemManager(database)
    # Add a MovementSystem instance to the world,
    # which implements the mechanics for Movable components.
    # It uses the entity manager, provided to it by the system manager,
    # to find and act on Movable components.
    game.add_system(AIattack())
    game.add_system(AImove())
    game.add_system(Display())

    try:
        while True:
            # Runs the update() method of all added systems.
            game.update(1)
            phealt = database.component_for_entity(player, Health)
            s = str(phealt.hp) + "/" + str(phealt.max_hp) + "> "
            input = raw_input(s)
            parser(database, player, input)
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
