from pysc2.lib.actions import FUNCTIONS

class Action:
    def __init__(self, group, priority):
        self.commands = []  # FunctionCall from pysc2.lib.actions
        self.idn = 0
        self.group = group
        self.priority = priority

    def __eq__(self, other):
        return self.group == other.group and self.commands == other.commands

    @classmethod
    def build_SCV(cls, cc):
        action = cls(cc, 5)
        action.commands.append(cc.select())
        action.commands.append(FUNCTIONS.Train_SCV_quick([False]))
