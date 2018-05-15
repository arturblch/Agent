import pytest
from model.Group import Group
from model.Unit import Unit

from pysc2.lib.features import PlayerRelative
from pysc2.lib import units

def test_group_add_units():
    group = Group()

    u1 = Unit(1, 1)
    u2 = Unit(2, 2)
    u3 = Unit(3, 3)

    group.addUnit(u1)
    group.addUnit(u2)
    group.addUnit(u3)

    assert group.unitList == [u1, u2, u3]
    assert group.getX() == 2 # mass X
    assert group.getY() == 2 # mass Y

def test_group_renew():
    group = Group()

    u1 = Unit(1, 1)
    group.addUnit(u1)
    assert group.unitList == [u1]

    u2 = Unit(2, 2)
    group.renew([u2])
    assert group.unitList == [u2]

