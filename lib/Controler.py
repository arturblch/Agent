from lib.Handler import BaseHandler
from lib.Handler import MoveToBeaconHandler

class Controler:
    def __init__(self, strategy):
        self._actMgr = strategy.actMgr
        self._handlers = []

    def addHandler(self, handler):
        if isinstance(handler, BaseHandler):
            self._handlers.append(handler(self))

    def start(self, obs):
        for handler in self._handlers:
            handler.handle(obs)

    def reset(self):
        for handler in self._handlers:
            handler.reset()


class MoveToBeaconControler(Controler):
    def __init__(self, strategy):
        super(MoveToBeaconControler, self).__init__(strategy)
        self.addHandler(MoveToBeaconHandler(self))