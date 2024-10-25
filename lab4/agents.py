from agentsPrograms import *
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
from mazeProblemSolvingAgentProDrawClass import MazeProblemSolvingAgentProDraw


def ProblemSolvingMazeAgentBFS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

def ProblemSolvingMazeAgentBFSShow(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentProDraw(initState,WorldGraph,goalState,BestFirstSearchAgentProgramForShow())


def ProblemSolvingMazeAgentBREADTH_FS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BreadthFirstSearchGraph())

def ProblemSolvingMazeAgentBREADTH_FSShow(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentProDraw(initState,WorldGraph,goalState,BreadthFirstSearchGraphForShow())

def ProblemSolvingMazeAgentDFS(initState, WorldGraph, goalState):
    return MazeProblemSolvingAgentPro(initState, WorldGraph, goalState, DepthFirstSearchGraph())

def ProblemSolvingMazeAgentDLS(initState, WorldGraph, goalState, limit):
    return MazeProblemSolvingAgentPro(initState, WorldGraph, goalState, LimitedDepthFirstSearchGraph(limit))

