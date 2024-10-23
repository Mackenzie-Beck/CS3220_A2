# Task 4

from agents import ProblemSolvingMazeAgentUCS, ProblemSolvingMazeAgentBREADTH_FS, ProblemSolvingMazeAgentBFS
from mazeGraphClass import mazeGraph
from mazeProblemClass import MazeProblem
from myMazeData import makeMaze, defineMazeActions, makeMazeTransformationModel

# Create the maze graph
n = 7
a = makeMaze(n)
mazeActs = defineMazeActions(a)
maze = makeMazeTransformationModel(mazeActs)
maze_graph = mazeGraph(maze)

# Define initial and goal states
initial_state = (0, 0)
goal_state = (6, 6)  # Assuming the cheese is at the bottom-right corner

# Create the problem
maze_problem = MazeProblem(initial_state, goal_state, maze_graph)

# Create and run the UCS agent
ucs_agent = ProblemSolvingMazeAgentBFS(initial_state, maze_graph, goal_state)
ucs_solution = ucs_agent.search(maze_problem)

# Create and run the BFS agent
bfs_agent = ProblemSolvingMazeAgentBREADTH_FS(initial_state, maze_graph, goal_state)
bfs_solution = bfs_agent.search(maze_problem)

# Compare the performance
if ucs_solution and bfs_solution:
    ucs_cost = sum(maze_problem.path_cost(0, ucs_solution[i], ucs_solution[i+1], ucs_solution[i+2]) 
                   for i in range(0, len(ucs_solution) - 2, 2))
    bfs_cost = sum(maze_problem.path_cost(0, bfs_solution[i], bfs_solution[i+1], bfs_solution[i+2]) 
                   for i in range(0, len(bfs_solution) - 2, 2))
    
    print(f"UCS path cost: {ucs_cost}")
    print(f"BFS path cost: {bfs_cost}")
    
    if ucs_cost < bfs_cost:
        print("Uniform-cost Search agent is more productive (spends less performance).")
    elif bfs_cost < ucs_cost:
        print("Breadth-First Search agent is more productive (spends less performance).")
    else:
        print("Both agents have the same performance.")
else:
    print("One or both agents failed to find a solution.")