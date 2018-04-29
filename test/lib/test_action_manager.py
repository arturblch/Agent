import pytest

from lib.ActionManager import ActionManager
from model.Action import ActionBuilder
from model.constants import PRIORITY
from pysc2.lib.actions import FUNCTIONS


class TestActionManager:
    def test_add_action(self):
        action_manager = ActionManager()

        action_manager.addAction(ActionBuilder.buildSCV(5, 5), PRIORITY(2))
        action_manager.addAction(ActionBuilder.buildSCV(4, 4), PRIORITY(1))
        action_manager.addAction(ActionBuilder.buildSCV(3, 3), PRIORITY(0))

        assert action_manager.getQueueLen() == 3
       
    def test_pop_action(self):
        action_manager = ActionManager()

        action_manager.addAction(ActionBuilder.buildSCV(5, 5), PRIORITY(2))
        action_manager.addAction(ActionBuilder.buildSCV(4, 4), PRIORITY(1))
        action_manager.addAction(ActionBuilder.buildSCV(3, 3), PRIORITY(0))

        action_manager.popAction()
        action_manager.popAction()
        action_manager.popAction()

        assert action_manager.getQueueLen() == 0

    def test_priority_queue(self):
        action_manager = ActionManager()

        act1 = ActionBuilder.buildSCV(5, 5)
        act2 = ActionBuilder.buildSCV(4, 4)
        act3 = ActionBuilder.buildSCV(3, 3)

        action_manager.addAction(act1, PRIORITY(2))
        action_manager.addAction(act2, PRIORITY(1))
        action_manager.addAction(act3, PRIORITY(0))

        assert action_manager.popAction() == act3
        assert action_manager.popAction() == act2
        assert action_manager.popAction() == act1

    def test_print_list(self):
        action_manager = ActionManager()

        action_manager.addAction(ActionBuilder.buildSCV(5, 5), PRIORITY(2))
        action_manager.addAction(ActionBuilder.buildSCV(4, 4), PRIORITY(1))
        action_manager.addAction(ActionBuilder.buildSCV(3, 3), PRIORITY(0))

        action_manager.printActionList()

    def test_clear(self):
        action_manager = ActionManager()

        action_manager.addAction(ActionBuilder.buildSCV(5, 5), PRIORITY(2))
        action_manager.addAction(ActionBuilder.buildSCV(4, 4), PRIORITY(1))
        action_manager.addAction(ActionBuilder.buildSCV(3, 3), PRIORITY(0))

        action_manager.clear()
        assert action_manager.getQueueLen() == 0