from heapq import heappush, heappop


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
        heappush(self.action_queue, (action.prioruty, action))

    def renew_actions(self, groups, cur_tick):
        for prior, action in self.action_queue:
            group_id = action.group.get_id()
            if group_id in groups.keys():
                action.update(groups[group_id])
            else:
                # Groupe has disappeared, remove action
                self.action_queue.pop((prior, action))

    def next_command(self):
        func = self.cur_action.next() if self.cur_action else None
        if func:
            return func
        elif len(self.action_queue) > 0:
            self.cur_action = heappop(self.action_queue)
            return self.cur_action.next()
        return None


