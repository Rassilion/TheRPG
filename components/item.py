from ecs.models import Component


class Item(Component):
    pass


class Weapon(Component):
    pass


class Equip(Component):
    __slots__ = "weapon"

    def __init__(self, weapon=None):
        self.weapon = weapon


class Inventory(Component):
    __slots__ = "inv"

    def __init__(self, inv=1):
        self.inv = inv
