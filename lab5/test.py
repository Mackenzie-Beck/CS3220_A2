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

foodLocations = getAllFoodLocations(a)
goalState = (n-1, n-1)  # Finish point


# Find the most cost-optimal path to each food dot
foodPaths = []
currentState = initState


for food in foodLocations:
    print("food: ", food, "---------------------------------------------------------------------------------")
    #mp = MazeProblem(currentState, food, mazeWorldGraph)
    mazeAvailableActs = defineMazeAvailableActions(a)
    maze = makeMazeTransformationModel(mazeAvailableActs)
    mazeWorldGraph = mazeGraph(maze)
    if food is not None:    
        agent = ProblemSolvingMazeAgentAStarManhattan(currentState, mazeWorldGraph, food)
        print("Food: ", food)
        result = agent.run()  
        print("result: ", result)
        foodPaths.append(result)
        currentState = food
        a[food[0]][food[1]] = 1




# After collecting all food dots, find the path to the finish point
print("Final path ------------------------------------------------------")
print("currentState: ", currentState)
mazeAvailableActs = defineMazeAvailableActions(a)
maze = makeMazeTransformationModel(mazeAvailableActs)
mazeWorldGraph = mazeGraph(maze)
#mp_final = MazeProblem(currentState, goalState, mazeWorldGraph)
agent_final = ProblemSolvingMazeAgentAStarManhattan(currentState, mazeWorldGraph, goalState)
result = agent_final.run()  
print("result: ", result)
# print("Final path found: ", finalPath)


# Combine all paths
completePath = []

for path in foodPaths:
    completePath.append(path)
completePath.append(result)



print("Complete path: ", completePath)

print(a)
draw_maze(a)

import copy







# Define a unique value to represent the path in the maze
PATH_VALUE = 5

# Create a copy of the maze to modify
resolvedMaze = copy.deepcopy(a)

# # Mark the path in the maze
# for path in completePath:
#     if path is not None:
#         resolvedMaze[path.state[0], path.state[1]] = PATH_VALUE
#         print(path.state)

# # Draw the maze with the path
# draw_maze(resolvedMaze)
