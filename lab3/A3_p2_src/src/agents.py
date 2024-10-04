from agentsPrograms import *
from deliveryProblemSolvingAgentClass import deliveryProblemSolvingAgent
from deliveryProblemSolvingAgentProClass import deliveryProblemSolvingAgentPro




def ProblemSolvingDeliveryAgentBFS(initState,WorldGraph,goalState):
    return deliveryProblemSolvingAgent(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())


def ProblemSolvingDeliveryAgentBFSwithShow(initState,WorldGraph,goalState):
    pass


def ProblemSolvingDeliveryAgentBFS_Pro(initState,WorldGraph,goalState):
    return deliveryProblemSolvingAgentPro(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())
