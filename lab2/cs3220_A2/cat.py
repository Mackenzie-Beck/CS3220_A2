from agentClass import Agent

import collections

class Cat(Agent):
    def __init__(self, program=None):
        self.name = 'cat'
        Agent.__init__(self)