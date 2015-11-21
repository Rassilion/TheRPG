from ecs.models import Component


class Item(Component):
    pass


class Weapon(Component):
    __slots__ = "atk"

    def __init__(self, atk=0):
        self.atk = atk


class Equip(Component):
    __slots__ = "weapon"

    def __init__(self, weapon=None):
        self.weapon = weapon


class Inventory(Component):
    __slots__ = "inv"

    def __init__(self, inv={}):
        self.inv = inv

    def add_item(self, item):
        self.inv.append(item)
