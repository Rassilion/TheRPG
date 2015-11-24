from ecs.exceptions import NonexistentComponentTypeForEntity


def getvalueor0(eman, e, c):
    try:
        value = eman.component_for_entity(e, c).value
    except NonexistentComponentTypeForEntity:
        value = 0
    return value


from .action import Movement, Attack
from .display import Display
from .input import Input
from .env import Kill, SpawnMob
from .ai import AIMove
