from ecs.models import Component
import stats
from util import getvalueor0


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

    # return equiped items str value
    def getstr(self, eman):
        if self.weapon is None:
            return 0
        else:
            return getvalueor0(eman, self.weapon, stats.Str)


class Inventory(Component):
    __slots__ = "inv"

    def __init__(self, inv=1):
        """inventory item identifier"""
        self.inv = inv
