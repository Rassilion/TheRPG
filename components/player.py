from ecs.models import Component


class Player(Component):
    pass


class Name(Component):
    def __init__(self, name):
        self.name = name
