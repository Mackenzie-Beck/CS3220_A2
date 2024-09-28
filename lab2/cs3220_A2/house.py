from environmentClass import Environment
from locations import *

import random

class House(Environment):
    def __init__(self):
        super().__init__()
        self.things = [] # Empty list of things in the environment.

    #adding the thing in random location
    def add_thing(self, thing):
        self.things.append(thing)
        thing.location = self.default_location(thing)

    #output the list of things with their locations
    def list_things_location(self):
        for thing in self.things:
            print(thing, thing.location)

    #removing the thing from the env
    def remove_thing(self, thing):
        self.things.remove(thing)

    #the status of the env is unknown **
    '''
    def percept(self, agent):
        #Returns the agent's location, and the location status (Dirty/Clean).
        for thing in self.things:
            # if there is dirt in the same location as the agent while the agent is perceiving
            # the location is dirty
            if thing.name == 'dirt' and thing.location == agent.location:
                # loop through loc's in status and if the location is the same as the agent's location
                # set that loc to dirty and return the agent's location and 'Dirty'
                for loc in self.status:
                    if loc == agent.location:
                        loc = 'Dirty'
                        return agent.location, 'Dirty'
            else:
                # if there is no dirt in the location, the location is clean
                for loc in self.status:
                    if loc == agent.location:
                        loc = 'Clean'
                        return agent.location, 'Clean'
    '''

    def is_agent_alive(self, agent):
        return agent.alive

    def update_agent_alive(self, agent):
        if agent.performance <= 0:
            agent.alive = False
            print("Agent {} is dead.".format(agent))

    def execute_action(self, agent, action):
        #Check if agent alive, if so, execute action
        if self.is_agent_alive(agent):
            """Change agent's location and/or location's status;
            Track performance.
            Score 10 for each dirt cleaned; -1 for each move."""

            if action == 'MoveRight' and agent.location != loc_E:
                if agent.location == loc_A:
                    agent.location = loc_B
                elif agent.location == loc_B:
                    agent.location = loc_C
                elif agent.location == loc_C:
                    agent.location = loc_D
                else:
                    agent.location = loc_E
                agent.performance -= 1
                self.update_agent_alive(agent)
            elif action == 'MoveLeft' and agent.location != loc_A:
                if agent.location == loc_B:
                    agent.location = loc_A
                elif agent.location == loc_C:
                    agent.location = loc_B
                elif agent.location == loc_D:
                    agent.location = loc_C
                else:
                    agent.location = loc_D
                agent.performance -= 1
                self.update_agent_alive(agent)
            elif action == 'Eat':
                if self.status[agent.location] == 'Dirty':
                    agent.performance += 10
                self.status[agent.location] = 'Clean'

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([loc_A, loc_B, loc_C, loc_D, loc_E])