import random
from envProClass import environmentPro
from thingClass import Thing
from locations import *
from directions import *
from agents import Student, ITStaff,OfficeManager




class part3Env(environmentPro):
  def __init__(self):
    super().__init__()
    self.locations=[Room1_A, Room1_B, Room1_C, Room2_A, Room2_B, Room2_C]

  def default_location(self, thing):
    print("The item is starting in random location...")
    return random.choice(self.locations)
    
  def percept(self, agent):
    #return a list of things that are in our agent's location
    things = self.list_things_at(agent.location)
    return agent.location, agent.direction, things
  
  def execute_action(self, agent, action):
    #changes the state of the environment based on what the agent does.
    if self.is_agent_alive(agent):

      if action=='Go forward':
          # if right then check if agent is in rooms that require special actions
          if agent.direction==right:
            if agent.location == Room1_C:
                agent.location = Room2_C
                agent.direction = left
                agent.performance -= 1
            elif agent.location == Room2_C:
                agent.location = Room1_C
                agent.direction = left
                agent.performance -= 1
            # if not in special rooms, then move forward
            else:
                agent.location = tuple(map(sum, zip(agent.location, (0,1))))
                agent.performance -= 1
          # if left then just move forward because rules_match will take care of the special actions
          elif agent.direction==left:
             agent.location = tuple(map(sum, zip(agent.location, (0,-1))))
             agent.performance -= 1

      elif action == 'Give mail':
        items = self.list_things_at(agent.location, thingClass=OfficeManager)
        agent.performance += 3
        self.update_agent_alive(agent)
        print("The Agent decided to {} to {} at location: {}".format(action,items[0],agent.location))
        self.delete_thing(items[0])

      elif action == 'Give donuts':
        items = self.list_things_at(agent.location, thingClass=ITStaff)
        agent.performance += 3
        self.update_agent_alive(agent)
        print("The Agent decided to {} to {} at location: {}".format(action,items[0],agent.location))
        self.delete_thing(items[0])

      elif action == 'Give pizza':
        items = self.list_things_at(agent.location, thingClass=Student)
        agent.performance += 3
        self.update_agent_alive(agent)
        print("The Agent decided to {} to {} at location: {}".format(action,items[0],agent.location))
        self.delete_thing(items[0])

      elif action == 'Stop':
        agent.alive = False



      self.update_agent_alive(agent)
      print("The Agent decided to {} at location: {}".format(action,agent.location))
