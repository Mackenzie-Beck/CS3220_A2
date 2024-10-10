import collections

from problemSolvingAgentProgramClass import SimpleProblemSolvingAgentProgram
from graphProblemClass import GraphProblem

class p3deliveryProblemSolvingAgent(SimpleProblemSolvingAgentProgram):
    def __init__(self, initial_state=None, dataGraph=None, goal=None, program=None):    
        super().__init__(initial_state)
        self.dataGraph = dataGraph
        self.goal = goal

        if program is None or not isinstance(program, collections.abc.Callable):
            print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))

            def program(percept):
                return eval(input('Percept={}; action? '.format(percept)))

        self.program = program

    def update_state(self, state, percept):
        return percept

    def formulate_goal(self, state):
        if self.goal is not None:
            return self.goal
        else:
            print("No goal! can't work!")
            return None

    def formulate_problem(self, state, goal):
        problem = GraphProblem(state, goal, self.dataGraph)
        return problem

    def search(self, problem):
        pass