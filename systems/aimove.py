from random import randint
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from components import *


class AImove(System):
    """Movement system to update position of Movable components."""

    def update(self, dt):
        for e, ai in self.entity_manager.pairs_for_type(AI):
            try:
                vel = self.entity_manager.component_for_entity(e, Velocity)
                pos = self.entity_manager.component_for_entity(e, Position)
            except NonexistentComponentTypeForEntity:
                print("%s has a Movement but no Position component, cannot move it.", e)
                continue
            pos.x += vel.dx * dt * randint(-2, 2)
            pos.y += vel.dy * dt * randint(-2, 2)


class AIattack(System):
    def update(self, dt):
        for e, ai in self.entity_manager.pairs_for_type(AI):
            try:
                player, pla = next(self.entity_manager.pairs_for_type(Player))
                ppos = self.entity_manager.component_for_entity(player, Position)
                pos = self.entity_manager.component_for_entity(e, Position)
            except NonexistentComponentTypeForEntity:
                continue
            if pos.collision(ppos):
                aiwep = self.entity_manager.component_for_entity(e, Equip).weapon
                self.entity_manager.component_for_entity(player, Health).hp -=self.entity_manager.component_for_entity(aiwep, Weapon).atk
                pwep = self.entity_manager.component_for_entity(player, Equip).weapon
                self.entity_manager.component_for_entity(e, Health).hp -= self.entity_manager.component_for_entity(pwep, Weapon).atk
