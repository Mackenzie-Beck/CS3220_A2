from TrivialVacuumEnvironment2 import TrivialVacuumEnvironment2

class House(TrivialVacuumEnvironment2):
    def __init__(self):
        super().__init__()

    #Overriding percept to accommodate the needs of the Cat Agent.
    def percept(self, agent):
        for thing in self.things:
            if thing.name == 'mouse' and thing.location == agent.location:
                #placeholder
            elif thing.name == 'mouse' and thing.location == agent.location:
                #placeholder
            elif thing.name == 'dog' and thing.location == agent.location:
                #placeholder
            else:
                #placeholder