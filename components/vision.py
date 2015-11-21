from ecs.models import Component


class Vision(Component):
    __slots__ = "value"

    def __init__(self, value):
        """
        value -- int, vision range
        """
        self.value = value


class Visible(Component):
    pass
