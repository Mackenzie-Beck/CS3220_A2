'''Randomly choose one of the actions from the vacuum environment'''
from agentPrograms import *
from agentClass import Agent
from data import *
from rules import *

def RandomVacuumAgent():
    return Agent(RandomAgentProgram(actionList))


def TableDrivenVacuumAgent():
     return Agent(TableDrivenAgentProgram(table))

def ReflexAgent() :
  return Agent(ReflexAgentProgram(agentRules,interpret_input,rule_match))
