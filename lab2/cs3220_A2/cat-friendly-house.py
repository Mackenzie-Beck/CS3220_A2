from environmentClass import Environment
from locations import *

import random

class TrivialVacuumEnvironment2(Environment):
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

  def percept(self, agent):
    pass

  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print("Agent {} is dead.".format(agent))

  def execute_action(self, agent, action):
     pass

  def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([loc_A, loc_B])