import random
from envProClass import environmentPro
from thingClass import Thing
from locationsP3 import *
from directions import *
class part3Env(environmentPro):
  def __init__(self):
    super().__init__()
    self.locations=[Room1_A, Room1_B, Room1_C, Room2_A, Room2_B, Room2_C]
    self.directions=[up, down, left, right]

  def default_location(self, thing):
    print("The item is starting in random location...")
    return random.choice(self.locations)
    
  def percept(self, agent):
    #return a list of things that are in our agent's location
    things = self.list_things_at(agent.location)
    return agent.location,agent.direction, things
  
  def execute_action(self, agent, action):
    #changes the state of the environment based on what the agent does.
    pass