import pytest
from model.Action import Action
from model.constants import PRIORITY

from pysc2.lib.actions import FUNCTIONS


class TestAction:
    def test_equal(self):
        act1 = Action(None, FUNCTIONS.move_camera.function_type)
        act2 = Action(None, FUNCTIONS.move_camera.function_type)
        act3 = Action(None, FUNCTIONS.move_camera.function_type)
        act1.commands.append(FUNCTIONS.move_camera([[1, 2]]))
        act2.commands.append(FUNCTIONS.move_camera([[1, 2]]))
        act3.commands.append(FUNCTIONS.move_camera([[1, 3]]))

        assert act1 == act2
        assert act1 != act3
