# This file about actiion managment for agent
class ActionManager:
    def __init__(self):
        self.tick = 0
        self.cur_action = None
        self.last_action = None
        self.action_tick = 0

        self.action_queue = []

    def add_action(self, action):
        for delay_actions in self.action_queue:
            if delay_actions.equal(action):
                self.action_queue.remove(delay_actions)
        self.action_queue.add(action)
        return True


    def execute_delay_move(self, move, world):
        move = self.cur_action.execute() if self.cur_action else None
        if move:
            return move
        elif (len(self.action_queue) > 0):
            self.cur_action = self.action_queue.pop(0)
            move = self.cur_action.execute()
        else:
            return None