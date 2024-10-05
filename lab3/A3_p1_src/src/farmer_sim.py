from farmer_problem import FarmerProblem
from agentsPrograms import BestFirstSearchAgentProgram

def simulate_farmer_problem():
    # Create an instance of the FarmerProblem
    problem = FarmerProblem()

    # Create a BestFirstSearchAgentProgram
    agent = BestFirstSearchAgentProgram()

    # Run the agent program on the problem
    solution = agent(problem)

    if solution:
        print("Solution found!")
        print("Path to solution:")
        path = solution.path()
        for node in path:
            print(f"State: {node.state}, Action: {node.action}")
        print(f"Total cost: {solution.path_cost}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    simulate_farmer_problem()
