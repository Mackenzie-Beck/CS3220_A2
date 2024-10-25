import random
from agentsPrograms import DepthFirstSearchGraph, LimitedDepthFirstSearchGraph
from agents import ProblemSolvingMazeAgentDFS, ProblemSolvingMazeAgentDLS
from mazeGraphClass import mazeGraph
from MazeProblemTask6 import MazeProblem
from myMazeData import makeMaze, defineMazeActions, makeMazeTransformationModel

# Create the maze graph
n = 7
a = makeMaze(n)
mazeActs = defineMazeActions(a)
maze = makeMazeTransformationModel(mazeActs)
maze_graph = mazeGraph(maze)

# Define initial state
initial_state = (0, 0)

# Place the cheese in a random cell above the 4th level (row) of the Maze
goal_state = (random.randint(5, 6), random.randint(0, 6))

# Create the problem
maze_problem = MazeProblem(initial_state, goal_state, maze_graph)

# Create and run the DFS agent
dfs_agent = ProblemSolvingMazeAgentDFS(initial_state, maze_graph, goal_state)
dfs_solution = dfs_agent.search(maze_problem)


# Create and run the DLS agent with a limit of 10
limit = 10
dls_agent = ProblemSolvingMazeAgentDLS(initial_state, maze_graph, goal_state, limit)
dls_solution = dls_agent.search(maze_problem)


# Compare the performance
if dfs_solution and dls_solution:
    dfs_cost = sum(maze_problem.path_cost(0, dfs_solution[i], dfs_solution[i+1], dfs_solution[i+2]) 
                   for i in range(0, len(dfs_solution) - 2, 2))
    dls_cost = sum(maze_problem.path_cost(0, dls_solution[i], dls_solution[i+1], dls_solution[i+2]) 
                   for i in range(0, len(dls_solution) - 2, 2))
    
    print(f"DFS path cost: {dfs_cost}")
    print(f"DLS path cost: {dls_cost}")
    
    if dfs_cost < dls_cost:
        print("Depth-First Search agent is more productive (spends less performance).")
    elif dls_cost < dfs_cost:
        print("Depth-Limited Search agent is more productive (spends less performance).")
    else:
        print("Both agents have the same performance.")
else:
    print("One or both agents failed to find a solution.")