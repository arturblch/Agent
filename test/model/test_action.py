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

    def test_add_command(self):
        act = Action(None, FUNCTIONS.move_camera.function_type)

        act.addCommand("Command_1")
        act.addCommand("Command_2")

        assert act.commands == ["Command_1", "Command_2"]

    def test_reset(self):
        act = Action(None, FUNCTIONS.move_camera.function_type)

        act.addCommand("Command_1")
        act.addCommand("Command_2")

        assert act.next() == "Command_1"
        assert act.next() == "Command_2"

        act.reset()
        assert act.next() == "Command_1"

