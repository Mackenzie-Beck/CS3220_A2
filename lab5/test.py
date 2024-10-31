from myMazeData import *
from agentsPrograms import A_StarSearchAgentProgram
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

foodLocations = getAllFoodLocations(a)
goalState = (n-1, n-1)  # Finish point

testfood = getFoodLocation(a)
# Find the most cost-optimal path to each food dot
foodPaths = []
currentState = initState


for food in foodLocations:
    mp = MazeProblem(currentState, food, mazeWorldGraph)
    agent = A_StarSearchAgentProgram(manhattanDistance.calc)
    print("Food: ", food)
    path = agent(mp)
    foodPaths.append(path)
    currentState = food


print("Food paths: ", foodPaths)

# After collecting all food dots, find the path to the finish point
mp_final = MazeProblem(currentState, goalState, mazeWorldGraph)
agent_final = A_StarSearchAgentProgram(manhattanDistance.calc)
finalPath = agent_final(mp_final)
print("Final path found: ", finalPath)


# Combine all paths
completePath = []
for path in foodPaths:
    completePath.append(path)
completePath.append(finalPath)



print("Complete path: ", completePath)

print(a)
draw_maze(a)

import copy
resolvedMaze=copy.deepcopy(a)

# i=3
# for node in completePath:
#     resolvedMaze[node.state[0],node.state[1]]=i
#     i+=1


# draw_maze(resolvedMaze)
