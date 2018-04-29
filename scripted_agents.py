from lib import ActionManager

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features
import numpy as np

CommandCenter = 18


class MoveToBeacon(base_agent.BaseAgent):
    """An agent specifically for solving the MoveToBeacon map."""

    def setup(self, obs_spec, action_spec):
        super(MoveToBeacon, self).setup(obs_spec, action_spec)
        self.actionMgr = ActionManager()

    def reset(self):
        super(MoveToBeacon, self).reset()
        self.actionMgr.clear()

    def step(self, obs):
        super(MoveToBeacon, self).step(obs)

        self.move()

        return self.actionMgr.next_command()

    def move(self):   
        if FUNCTIONS.Move_screen.id in obs.observation.available_actions:
          player_relative = obs.observation.feature_screen.player_relative
          beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)
          if not beacon:
            return FUNCTIONS.no_op()
          beacon_center = numpy.mean(beacon, axis=0).round()
          return FUNCTIONS.Move_screen("now", beacon_center)
        else:
          return FUNCTIONS.select_army("select")