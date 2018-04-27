from model.constants import 

from pysc2.lib.actions import FUNCTIONS

class Action:
    def __init__(self, group):
        self.group = group
        self.idn = 0
        self.types = []
        self.commands = []  # FunctionCall from pysc2.lib.actions

    def __eq__(self, other):
        return self.group == other.group and self.types == other.types

    def next(self):
        command = self.getCommand(self.idn)
        self.idn += 1
        return command

    def reset(self):
        self.idn = 0

    def getCommand(self, idn):
        if idn >= len(self.commands):
            return None
        return self.commands[self.idn]

    def addCommand(self, command):
        self.commands.append(command)
        self.types.append(command.function_type.__name__)

    def __repr__(self):
        return 'Action<group={}, type={}>'.format(self.group, self.type)

    
class ActionBuilder:
    @staticmethod
    def buildSCV(x1, y1):
        action = Action(None, FUNCTIONS.Train_SCV_quick.function_type)
        action.commands.append(FUNCTIONS.select_point("select", [x1, y1]))
        action.commands.append(FUNCTIONS.Train_SCV_quick("now"))
        return action