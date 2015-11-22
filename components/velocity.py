import math
from ecs.models import Component


class Velocity(Component):
    def __init__(self, dx=0., dy=0.):
        """velocity data"""
        self.dx = dx
        self.dy = dy

    @property
    def velocity(self):
        return self.dx, self.dy
