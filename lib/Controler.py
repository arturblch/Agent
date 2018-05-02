from lib.Handler import BaseHandler

class Controler:
    def __init__(self, strategy):
        self._actMgr = strategy.actMgr
        self._handlers = []

    def addHandler(self, handler):
        if isinstance(handler, BaseHandler):
            self._handlers.append(handler(self._actMgr))

    def start(self, obs):
        for handler in self._handlers:
            handler.handle(obs)

    def reset(self):
        for handler in self._handlers:
            handler.reset()
