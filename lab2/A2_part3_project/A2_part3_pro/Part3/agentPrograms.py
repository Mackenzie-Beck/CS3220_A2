'''An idea of Random Agent Program is to choose an action at random, ignoring all percepts'''
from locations import *
from agents import Student, ITStaff,OfficeManager




def ReflexAgentProgram(rules,interpret_input,rule_match):
  #This AP takes action based solely on the percept.
    
    def program(percept):
        state = interpret_input(percept)
        action = rule_match(state, rules)
        return action

    return program


def interpret_input(percept):
  loc, status = percept
  return status


def rule_match(state, rules):
  for key in rules:
    if state in key:
      return rules[key]




def interpret_input_a2p3Rules(percept):
  # this is where the agent interprets its percept and updates env
  loc, things = percept
  pass
def rule_match_a2p3(state, rules):
  # this is where the agent selects an action based on its state and rules
  pass






def interpret_input_A2pro(percept):
  loc, percepts = percept
  #print(percepts,loc, loc_D)
  status='Clear'
  if len(percepts)==0:
    if loc==loc_D:
      status='Last room'
      #print(1)
  else:
    for p in percepts:
      if isinstance(p, OfficeManager):
        return 'Office manager'
      elif isinstance(p, ITStaff):
        return 'IT'
      elif isinstance(p, Student):
        return 'Student'
  print(status)
  return status

def rule_match_A2pro(state, rules):
  return rules[state]


'''def ReflexAgentProgram_A2pro(rules,interpret_input,rule_match):
  def program(percept):
    state = interpret_input(percept)
    action = rule_match(state, rules)
    return action

    return program'''


