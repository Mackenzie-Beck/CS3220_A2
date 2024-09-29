'''Randomly choose one of the actions from the vacuum environment'''
from agentClass import Agent
from agentPrograms import RandomAgentProgram, TableDrivenAgentProgram
from lookuptable import feedingRules





def agent_cat():
    return Agent(TableDrivenAgentProgram(feedingRules))



def RandomVacuumAgent():
    return Agent(RandomAgentProgram(actionList))


def TableDrivenVacuumAgent():
     return Agent(TableDrivenAgentProgram(table))