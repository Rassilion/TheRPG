from ecs.models import Component


class Item(Component):
    """item identifier"""
    pass


class Weapon(Component):
    """weapon identifier"""
    pass


class Equip(Component):
    __slots__ = "weapon"

    def __init__(self, weapon=None):
        """equipped items of character"""
        self.weapon = weapon


class Inventory(Component):
    __slots__ = "inv"

    def __init__(self, inv=1):
        """inventory item identifier"""
        self.inv = inv
