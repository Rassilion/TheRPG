#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from ecs import EntityManager, SystemManager
from components import *
from systems import *


def main():
    # Create an entity manager, a database entities and components.
    database = EntityManager()
    # Create a player entity.
    player = database.create_entity()
    wep1 = database.create_entity()
    # Add components
    database.add_component(wep1, Weapon())
    database.add_component(wep1, Item())
    database.add_component(wep1, Str(10))
    database.add_component(wep1, Name("Basic Sword"))

    database.add_component(player, Position(x=10, y=10))
    database.add_component(player, Velocity())
    database.add_component(player, Player())
    database.add_component(player, Name("Ra"))
    database.add_component(player, Health(10000))
    database.add_component(player, Str(10))
    database.add_component(player, Def(10))
    database.add_component(player, Vision(10))
    database.add_component(player, Visible())
    database.add_component(player, Equip(weapon=wep1))

    pos = [Position(x=15, y=20), Position(x=11, y=10), Position(x=16, y=19)]

    for p in pos:
        mob1 = database.create_entity()
        database.add_component(mob1, p)
        database.add_component(mob1, Velocity(1, 1))
        database.add_component(mob1, AI())
        database.add_component(mob1, Name("Mob" + str(mob1._guid)))
        database.add_component(mob1, Health(100))
        database.add_component(mob1, Str(15))
        database.add_component(mob1, Def(1))
        database.add_component(mob1, Visible())
        database.add_component(mob1, Vision(5))
        database.add_component(mob1, Equip(weapon=wep1))

    # Create a system manager, i.e. the game world.
    game = SystemManager(database)

    # add systems
    game.add_system(Movement())
    game.add_system(Attack())
    game.add_system(Kill())
    game.add_system(SpawnMob())
    game.add_system(Display())
    game.add_system(Input())
    game.add_system(AIMove())

    try:
        while True:
            # Runs the update() method of all added systems.
            game.update(1)
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
