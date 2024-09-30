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
    thing_at_location = self.list_things_location(agent.location)
    if thing_at_location and isinstance(thing_at_location, Sausage):
      status = "SausageHere"
    elif thing_at_location and isinstance(thing_at_location, Milk):
      status = "MilkHere"
    return(agent.location, status)

  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance <= 0:
      agent.alive = False
      print("Agent {} is dead.".format(agent))

  def execute_action(self, agent, action):
     if self.is_agent_alive(agent):
        if action == "moveright":
           agent.location += 1
           agent.performance -= 1
           self.update_agent_alive(agent)
        elif action == "moveleft":
           agent.location -= 1
           agent.performance -= 1
           self.update_agent_alive(agent)


        # eating and drinking give performance equal to the calories of the food divided by the weight
        # assignment didnt really specify how the two should affect eachother but I think that works
        elif action == "eat":
           sausage = self.list_things_location(agent.location)
           agent.performance += sausage.calories // sausage.weight
           self.remove_thing(sausage)
           
        elif action == "drink":
           milk = self.list_things_location(agent.location)
           agent.performance += milk.calories // milk.weight
           self.remove_thing(milk)
        elif action == "stop":
            agent.alive = False

  def default_location(self, thing):
        """Agents start in either location at random."""
        room = random.choice([room1, room2, room3])
        if self.list_things_location(room) is None:
            return room
        else:
            return self.default_location(thing)
