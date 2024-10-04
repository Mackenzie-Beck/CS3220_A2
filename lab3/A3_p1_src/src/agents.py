from agentsPrograms import *
from vacuumProblemSolvingAgentProClass import VacuumProblemSolvingAgentPro
from vacuumProblemSolvingAgentShowClass import VacuumProblemSolvingAgentDraw


def ProblemSolvingVacuumAgentBFS(initState,vacuumWorldGraph,goalState):
    return VacuumProblemSolvingAgentPro(initState,vacuumWorldGraph,goalState,BestFirstSearchAgentProgram())


def ProblemSolvingVacuumAgentBFSwithShow(initState,vacuumWorldGraph,goalState):
    return VacuumProblemSolvingAgentDraw(initState,vacuumWorldGraph,goalState,BestFirstSearchAgentProgramForShow())