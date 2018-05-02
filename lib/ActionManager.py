from heapq import heappush, heappop
from model.constants import PRIORITY


class ActionManager:
    """ActionManager provide access to action queue
    """
    def __init__(self):
        self.tick = 0
        self.last_actions = dict()
        self.action_queue = []

    # TODO(arturblch): check if action was in past
    def addAction(self, action, prioruty=PRIORITY(4)):
        heappush(self.action_queue, (prioruty, action))

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
            _, self.cur_action = heappop(self.action_queue)
            return self.cur_action.next()
        return None

    def popAction(self):
        _, action= heappop(self.action_queue)
        return action

    def getQueueLen(self):
        return len(self.action_queue)

    def clear(self):
        self.last_actions.clear()
        self.action_queue.clear()

    def printActionList(self):
        for _, action in self.action_queue:
            print(action)
