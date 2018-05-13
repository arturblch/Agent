from pysc2.lib.actions import FUNCTIONS

class Action:
    def __init__(self, group=None):
        self.group = group
        self.idn = 0
        self.ids = []
        self.commands = []  # FunctionCall from pysc2.lib.actions

    def __eq__(self, other):
        return self.group == other.group and self.ids == other.ids

    def __repr__(self):
        return 'Action<group={}, ids={}>'.format(self.group, self.ids)

    @property
    def commandsCount(self):
        return len(self.commands)

    def next(self):
        if self.idn >= self.commandsCount:
            return None
        command = self.commands[self.idn]
        self.idn += 1
        return command

    def reset(self):
        self.idn = 0

    def getCommand(self, idn):
        if idn >= self.commandsCount:
            return None
        return self.commands[self.idn]

    def addCommand(self, command):
        self.commands.append(command)
        if hasattr(command, 'function'):
            self.ids.append(command.function)
        else:
            self.ids.append(None)

    
class ActionBuilder:
    @staticmethod
    def buildSCV(x1, y1):
        action = Action()
        action.addCommand(FUNCTIONS.select_point("select", [x1, y1]))
        action.addCommand(FUNCTIONS.Train_SCV_quick("now"))
        return action

    @staticmethod
    def moveCamera(x1, y1):
        action = Action()
        action.addCommand(FUNCTIONS.move_camera([x1, y1]))
        return action

    @staticmethod
    def moveScreen(x1, y1):
        action = Action()
        action.addCommand(FUNCTIONS.Move_screen("now", [x1, y1]))
        return action

    @staticmethod
    def noOp():
        action = Action()
        action.addCommand(FUNCTIONS.no_op())
        return action

    def selectArmy():
        action = Action()
        action.addCommand(FUNCTIONS.select_army("select"))
        return action
