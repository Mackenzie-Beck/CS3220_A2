from farmer_problem import FarmerProblem
from agentsPrograms import BestFirstSearchAgentProgram
import networkx as nx
import matplotlib.pyplot as plt
from visualGraph1 import drawGraph

def simulate_farmer_problem():
    # Create an instance of the FarmerProblem
    problem = FarmerProblem()

    # Create a BestFirstSearchAgentProgram
    agent = BestFirstSearchAgentProgram()

    # Run the agent program on the problem
    solution = agent(problem)

    # Track node statuses
    node_statuses = {node: 'unexplored' for node in problem.graph.keys()}
  #  print(node_statuses)

    if solution:
        print("Solution found!")
        print("Path to solution:")
        path = solution.path()


        for node in path:
            print(f"State: {node.state}, Action: {node.action}")
            node_statuses[node.state] = 'goal' if node.state == problem.goal_state else 'expanded'
        print(f"Total cost: {solution.path_cost}")
    else:
        print("No solution found.")

    # Visualize the graph
    drawGraph(problem, nodeColors={}, steps=0)
    print(node_statuses)

if __name__ == "__main__":
    simulate_farmer_problem()
