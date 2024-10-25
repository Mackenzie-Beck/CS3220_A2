from agentsPrograms import *

import unittest
from mazeProblemClass import MazeProblem
from mazeGraphClass import mazeGraph
from myMazeData import makeMaze, defineMazeActions, makeMazeTransformationModel

class TestDFSFunctions(unittest.TestCase):

    def setUp(self):
        # Create the maze graph
        n = 7
        a = makeMaze(n)
        mazeActs = defineMazeActions(a)
        maze = makeMazeTransformationModel(mazeActs)
        self.maze_graph = mazeGraph(maze)

        # Define initial and goal states
        self.initial_state = (0, 0)
        self.goal_state = (6, 6)  # Assuming the cheese is at the bottom-right corner

        # Create the problem
        self.maze_problem = MazeProblem(self.initial_state, self.goal_state, self.maze_graph)

    def test_DepthFirstSearchGraph(self):
        dfs_agent = DepthFirstSearchGraph()
        solution = dfs_agent(self.maze_problem)
        self.assertIsNotNone(solution, "DFS agent failed to find a solution.")
        self.assertTrue(self.maze_problem.goal_test(solution.state), "DFS agent did not reach the goal state.")

    def test_LimitedDepthFirstSearchGraph(self):
        limit = 10
        ldfs_agent = LimitedDepthFirstSearchGraph(limit)
        solution = ldfs_agent(self.maze_problem)
        self.assertIsNotNone(solution, "Limited DFS agent failed to find a solution within the limit.")
        self.assertTrue(self.maze_problem.goal_test(solution.state), "Limited DFS agent did not reach the goal state within the limit.")

if __name__ == '__main__':
    unittest.main()
