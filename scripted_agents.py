from lib.ActionManager import ActionManager
from lib.Controler import MoveToBeaconControler

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features


CommandCenter = 18


class MoveToBeacon(base_agent.BaseAgent):
    """An agent specifically for solving the MoveToBeacon map."""

    def setup(self, obs_spec, action_spec):
        super(MoveToBeacon, self).setup(obs_spec, action_spec)
        self.actMgr = ActionManager()
        self.controler = MoveToBeaconControler(self)

    def reset(self):
        super(MoveToBeacon, self).reset()
        self.actMgr.clear()

    def step(self, obs):
        super(MoveToBeacon, self).step(obs)

        self.controler.start(obs)

        return self.actMgr.nextCommand()