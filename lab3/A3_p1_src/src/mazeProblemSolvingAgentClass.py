from problemSolvingAgentProgramClass import SimpleProblemSolvingAgentProgram
from mazeProblemClass import MazeProblem

class MazeProblemSolvingAgent(SimpleProblemSolvingAgentProgram):
    def __init__(self, initial_state = None, dataGraph = None, goal = None):
        super().__init__(initial_state)
        self.dataGraph = dataGraph
        self.goal = goal
        self.performance = len(dataGraph.nodes()) // 2 # 16 performance

    def update_state(self, state, percept):
        return percept

    def formulate_goal(self, state):
        if self.goal is not None:
            return self.goal
        else:
            print("No goal! can't work!")
            return None
    
    def formulate_problem(self, state, goal):
        problem = MazeProblem(state, goal, self.dataGraph)
        return problem
    
    def search(self, problem):
        pass

    def new_goal(self, initial_state, goal):
        super().__init__(initial_state)
        self.goal = goal