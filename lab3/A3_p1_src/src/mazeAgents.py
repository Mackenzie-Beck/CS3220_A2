from agentsPrograms import *
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
from mazeProblemSolvingAgentShowClass import MazeProblemSolvingAgentDraw


def ProblemSolvingMazeAgentBFS(initState,mazeWorldGraph,goalState):
    return MazeProblemSolvingAgentPro(initState,mazeWorldGraph,goalState,BestFirstSearchAgentProgram())


def ProblemSolvingMazeAgentBFSwithShow(initState,mazeWorldGraph,goalState):
    return MazeProblemSolvingAgentDraw(initState,mazeWorldGraph,goalState,BestFirstSearchAgentProgramForShow())