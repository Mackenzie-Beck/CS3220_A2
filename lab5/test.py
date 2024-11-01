from myMazeData import *
from agentsPrograms import *
from mazeGraphClass import mazeGraph
from mazeProblemClass import MazeProblem
from agents import *
from drawmaze import draw_maze
n = 10
a = makeMaze(n)


mazeAvailableActs = defineMazeAvailableActions(a)
maze = makeMazeTransformationModel(mazeAvailableActs)
mazeWorldGraph = mazeGraph(maze)

initState = (0,0)
finalState = (n-1, n-1)
goalStates = getAllFoodLocations(a)
goalStates.append(finalState)
print(goalStates)


a1 = ProblemSolvingMazeAgentAStarManhattan(initState, mazeWorldGraph, goalStates)


s,p = a1.run()

draw_maze(a)


import copy
resolvedMaze=copy.deepcopy(a)
i=3
for path in p:
  for node in path:
     resolvedMaze[node.state[0],node.state[1]]=i
  i+=1


print(a)
print(resolvedMaze)