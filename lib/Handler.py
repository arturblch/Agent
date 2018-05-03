import numpy

from pysc2.lib.actions import FUNCTIONS
from model.Action import ActionBuilder


def _xy_locs(mask):
  """Mask should be a set of bools from comparison with a feature layer."""
  y, x = mask.nonzero()
  return list(zip(x, y))


class BaseHandler:
    def __init__(self, controler=None):
        self.controler = controler

    def handle(self, obs):
        raise NotImplemented

    def reset(self):
        raise NotImplemented

    def controlAction(self, action):
        self.controler._actMgr.addAction(action)



class MoveToBeaconHandler(BaseHandler):
    def __init__(self, controler):
        super(MoveToBeaconHandler, self).__init__(controler)
        self.selected = False

    def handle(self, obs)
        self.selected = FUNCTIONS.Move_screen.id in obs.observation.available_actions

        if not self.selected:
            self.controlAction(ActionBuilder.selectArmy())
            return False
        else:
            player_relative = obs.observation.feature_screen.player_relative
            beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)
            if not beacon:
                self.controlAction(ActionBuilder.noOp())
                return False
            beacon_center = numpy.mean(beacon, axis=0).round()
            self.controlAction(ActionBuilder.moveScreen("now", beacon_center))
            return True

    def reset(self):
        self.selected = False