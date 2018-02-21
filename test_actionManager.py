import pytest
from action_manager import ActionManager
from action import Action
from action import PRIORITY

from pysc2.lib.actions import FUNCTIONS


class TestActionManager:
    def test_add_action(self):
        action_manager = ActionManager()
        act1 = Action.buildSCV(30, 30, 34, 34)
        act2 = Action.buildSCV(30, 30, 34, 34)
        act3 = Action.buildSCV(30, 3, 34, 34)

        action_manager.add_action(act1)
        action_manager.add_action(act2)
        action_manager.add_action(act3)

        assert len(action_manager.action_queue) == 2


    def test_next_command(self):
        action_manager = ActionManager()
        act1 = Action(None, FUNCTIONS.move_camera.function_type, PRIORITY.NORMAL)
        act2 = Action(None, FUNCTIONS.move_camera.function_type, PRIORITY.NORMAL)
        act1.commands.append(FUNCTIONS.move_camera([[1, 2]]))
        act2.commands.append(FUNCTIONS.move_camera([[3, 4]]))

        action_manager.add_action(act1)
        action_manager.add_action(act2)

        assert action_manager.next_command == FUNCTIONS.move_camera([[1, 2]])
        assert action_manager.next_command == FUNCTIONS.move_camera([[3, 4]])
        assert action_manager.next_command is None


