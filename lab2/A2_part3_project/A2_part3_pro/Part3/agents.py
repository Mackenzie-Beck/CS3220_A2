'''Randomly choose one of the actions from the vacuum environment'''

from thingClass import Thing
from rules import *




class OfficeManager(Thing):
  def __init__(self):
    super().__init__()
    self.name = "Office Manager"

class ITStaff(Thing):
    def __init__(self):
      super().__init__()
      self.name = "IT Staff"

class Student(Thing):
    def __init__(self):
        super().__init__()
        self.name = "Student"


from agentClass import Agent
from agentPrograms import *
def ReflexAgentP3() :
  return Agent(ReflexAgentProgram(a2p3Rules,interpret_input_a2p3Rules,rule_match_a2p3))


"""def ReflexAgentA2pro() :
  return Agent(ReflexAgentProgram(a2proRules,interpret_input_A2pro,rule_match_A2pro))"""
