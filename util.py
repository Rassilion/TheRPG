from ecs.exceptions import NonexistentComponentTypeForEntity


def getvalueor0(eman, e, c):
    try:
        value = eman.component_for_entity(e, c).value
    except NonexistentComponentTypeForEntity:
        value = 0
    return value
