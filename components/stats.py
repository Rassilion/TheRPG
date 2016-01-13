from ecs.models import Component


class Health(Component):
    __slots__ = "hp", "max_hp"

    def __init__(self, max_hp):
        """
        max_hp -- int, health points this entity can have at most
        """
        self.hp = max_hp
        self.max_hp = max_hp

    def decreasehealt(self, int):
        if int > 0:
            self.hp = max(self.hp - int, 0)

    def increasehealt(self, int):
        self.hp = min(self.hp + int, self.max_hp)


class Str(Component):
    __slots__ = "value"

    def __init__(self, str=10):
        """strength value"""
        self.value = str


class Def(Component):
    __slots__ = "value"

    def __init__(self, d=10):
        """defence value"""
        self.value = d
