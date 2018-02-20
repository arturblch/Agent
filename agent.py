from pysc2.agents import base_agent
from pysc2.lib import actions

CommandCenter = 18

class Agent(base_agent.BaseAgent):

    def step(self, obs):
        super().step(obs)
        if obs.first():
            for x in range(84):
                print(obs.observation["feature_screen"].height_map[x, ])
        return actions.FUNCTIONS.no_op()

