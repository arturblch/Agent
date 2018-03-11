from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features
import numpy as np
import pickle

CommandCenter = 18


class Agent(base_agent.BaseAgent):

    def step(self, obs):
        super().step(obs)

        with open('D:\\Python\Agent\\pickle\\tick{}.pickle'.format(self.steps), 'wb') as handle:
            pickle.dump(obs, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return actions.FUNCTIONS.no_op()
