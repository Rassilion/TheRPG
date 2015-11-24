from ecs.models import Component


class Player(Component):
    """player identifier"""
    pass


class Name(Component):
    def __init__(self, name):
        """name component"""
        self.name = name
