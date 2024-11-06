import math
from agentsPrograms import *
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
from manhattanDistance import *
# from mazeProblemSolvingAgentProDrawClass import MazeProblemSolvingAgentProDraw

def ProblemSolvingMazeAgentAStar(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,A_StarSearchAgentProgram(math.dist))


def ProblemSolvingMazeAgentBFS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

# def ProblemSolvingMazeAgentBFSShow(initState,WorldGraph,goalState):
#     return MazeProblemSolvingAgentProDraw(initState,WorldGraph,goalState,BestFirstSearchAgentProgramForShow())


def ProblemSolvingMazeAgentBREADTH_FS(initState,WorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,WorldGraph,goalState,BreadthFirstSearchGraph())


def ProblemSolvingMazeAgentAStarManhattan(initState, WorldGraph, goalState):
    return MazeProblemSolvingAgentPro(initState, WorldGraph, goalState, A_StarSearchAgentProgram(manhattanDistance.calc))


def ProblemSolvingMazeAgentIDAStar(initState, WorldGraph, goalState):
    return MazeProblemSolvingAgentPro(initState, WorldGraph, goalState, IDA_StarSearchAgentProgram(math.dist))


def ProblemSolvingMazeAgentIDAStarManhattan(initState, WorldGraph, goalState):
    return MazeProblemSolvingAgentPro(initState, WorldGraph, goalState, IDA_StarSearchAgentProgram(manhattanDistance.calc))


def ProblemSolvingMazeAgentIDAStarManhattan(initState, WorldGraph, goalState):
    return MazeProblemSolvingAgentPro(initState, WorldGraph, goalState, IDA_StarSearchAgentProgram(manhattanDistance.calc))
