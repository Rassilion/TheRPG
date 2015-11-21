from ecs.models import Component


class Vision(Component):
    __slots__ = "range"

    def __init__(self, range):
        """
        range -- int, vision range
        """
        self.range = range
