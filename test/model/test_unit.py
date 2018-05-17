import pytest
from model.Unit import Unit
from pysc2.lib.units import Terran


def test_unit_creation():
    _x = 1
    _y = 1
    _hp = 5
    _typeId = Terran.SCV
    unit = Unit(x=_x, y=_y, hp=_hp, typeId=_typeId, idn=0)

    assert unit.getX() == _x
    assert unit.getY() == _y
    assert unit.getHp() == _hp
    assert unit.getTypeId() == _typeId

def test_get_distance():
    unit = Unit(x=0, y=0)

    point = [3, 4]
    assert unit.get_distance_to(*point) == 5

def test_get_distance_to_unit():
    unit1 = Unit(x=0, y=0)
    unit2 = Unit(x=3, y=4)

    assert unit1.get_distance_to_unit(unit2) == 5

def test_unit_change_invis():
    unit = Unit(x=0, y=0)

    assert unit.invis == False
    unit.changeInvis()
    assert unit.invis == True