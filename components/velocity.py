import math
from ecs.models import Component


class Velocity(Component):
    """Component for position and velocity data."""

    def __init__(self, dx=1, dy=1):
        self.dx = dx
        self.dy = dy

    @property
    def velocity(self):
        return self.dx, self.dy
