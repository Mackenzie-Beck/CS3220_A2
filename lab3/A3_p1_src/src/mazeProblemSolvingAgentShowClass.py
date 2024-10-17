from networkx.algorithms import shortest_simple_paths
from mazeProblemSolvingAgentProClass import MazeProblemSolvingAgentPro
#from visualGraph import drawGraph
from visualGraph1 import drawGraph

class MazeProblemSolvingAgentDraw(MazeProblemSolvingAgentPro):
    def search(self, problem):
      seq, steps, allNodeColors= self.program(problem)
      #print(len(allNodeColors))
      #print(allNodeColors)
      solution=self.actions_path(seq.path())
      print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))
      if len(seq.path()) >= self.performance:
        print("Agent will run out of performance taking this path!")
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
