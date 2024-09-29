from environmentClass import Environment
from locations_cfh import *
from milk import Milk
from sausage import Sausage

import random

class CatFriendlyHouse(Environment):
  def __init__(self):
    super().__init__()
    self.things = [] # Empty list of things in the environment.

  #adding the thing in random location
  def add_thing(self, thing):
    self.things.append(thing)
    thing.location = self.default_location(thing)

  #output the thing which is at a given location
  def list_things_location(self, location):
    for thing in self.things:
        if thing.location == location:
           return thing

  #removing the thing from the env
  def remove_thing(self, thing):
    self.things.remove(thing)

  #the status of the env is unknown **

  def percept(self, agent):
    #Returns the agent's location, and the location status (SausageHere/MilkHere/Empty).
    status = "Empty"
    if self.list_things_location(agent.location).isinstance(Sausage):
      status = "SausageHere"
    elif self.list_things_location(agent.location).isinstance(Milk):
      status = "MilkHere"
    return(agent.location, status)

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
        return random.choice([room1, room2, room3])