from pysc2.lib.actions import FUNCTIONS
from enum import Enum


class PRIORITY(Enum):
    URGENTLY = 0
    QUICKLY = 1
    NORMAL = 2
    LOW = 3

class Action:
    def __init__(self, group, type, priority):
        self.group = group
        self.type = type
        self.priority = priority
        self.idn = 0
        self.commands = []  # FunctionCall from pysc2.lib.actions

    def __eq__(self, other):
        return self.group == other.group and self.commands == other.commands

    def next(self):
        command = self.getCommand(self.idn)
        self.idn += 1
        return command

    def getCommand(self, idn):
        if idn >= len(self.commands):
            return None
        return self.commands[self.idn]

    @classmethod
    def createSelect(cls, x1, y1, x2, y2):
        command = FUNCTIONS.select_rect(False, [x1, y1], [x2, y2])
        return command


    @classmethod
    def buildSCV(cls, x1, y1, x2, y2):
        action = cls(None, FUNCTIONS.Train_SCV_quick.function_type, PRIORITY.NORMAL)
        action.commands.append(cls.createSelect(x1, y1, x2, y2))
        action.commands.append(FUNCTIONS.Train_SCV_quick(False))
        return action
