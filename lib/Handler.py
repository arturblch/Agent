from pysc2.lib.actions import FUNCTIONS
from model.Action import ActionBuilder
import numpy


def _xy_locs(mask):
  """Mask should be a set of bools from comparison with a feature layer."""
  y, x = mask.nonzero()
  return list(zip(x, y))


class BaseHandler:
    def __init__(self, actMgr=None):
        self._actMgr = actMgr

    def handle(self, obs):
        raise NotImplemented

    def reset(self):
        raise NotImplemented



class MoveToBeaconHandler(BaseHandler):
    def __init__(self, actMgr):
        super(MoveToBeaconHandler, self).__init__(actMgr)
        self.selected = False

    def handle(self, obs)
        self.selected = FUNCTIONS.Move_screen.id in obs.observation.available_actions

        if not self.selected:
            self._actMgr.addAction(ActionBuilder.selectArmy())
            return False
        else:
            player_relative = obs.observation.feature_screen.player_relative
            beacon = _xy_locs(player_relative == _PLAYER_NEUTRAL)
            if not beacon:
                self._actMgr.addAction(ActionBuilder.noOp())
                return False
            beacon_center = numpy.mean(beacon, axis=0).round()
            self._actMgr.addAction(ActionBuilder.moveScreen("now", beacon_center))
            return True

    def reset(self):
        self.selected = False