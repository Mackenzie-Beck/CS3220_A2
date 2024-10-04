from networkx.algorithms import shortest_simple_paths
from vacuumProblemSolvingAgentProClass import VacuumProblemSolvingAgentPro
from visualGraph import drawGraph

class VacuumProblemSolvingAgentDraw(VacuumProblemSolvingAgentPro):
    def search(self, problem):
      seq, steps, allNodeColors= self.program(problem)
      #print(len(allNodeColors))
      #print(allNodeColors)
      solution=self.actions_path(seq.path())
      print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))
      return (solution,steps, allNodeColors)

    def work(self, percept):
        #allNodeColors=[]
        #nSteps=0
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq, steps, allNodeColors = self.search(problem)
            #print(allNodeColors[steps-1])
            if not self.seq:
                return None
            drawGraph(self.dataGraph, allNodeColors[steps-1], steps)
        return self.seq
