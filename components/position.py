import math
from ecs.models import Component


class Position(Component):
    """Component for position and velocity data."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos(self):
        return int(self.x), int(self.y)

    def collision(self, pos):
        if self.x == pos.x and self.y == pos.y:
            return True
        else:
            return False
