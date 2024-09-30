from agentClass import Agent

class Cat(Agent):
    def __init__(self, program=None):
        self.name = 'cat'
        self.performance = 10
        Agent.__init__(self, program)