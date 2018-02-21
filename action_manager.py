# TODO(arturblch): add priority queue


class ActionManager:
    """ActionManager provide access to action queue
    """

    def __init__(self):
        self.tick = 0
        self.cur_action = None
        self.last_actions = dict()
        self.action_queue = []

    # TODO(arturblch): check if action was in past
    def add_action(self, action):
        if action in self.action_queue:
            self.action_queue.remove(action)
        self.action_queue.append(action)
        return True

    def renewActions(self):
        pass

    def next_command(self):
        func = self.cur_action.next() if self.cur_action else None
        if func:
            return func
        elif len(self.action_queue) > 0:
            self.cur_action = self.action_queue.pop(0)
            return self.cur_action.next()
