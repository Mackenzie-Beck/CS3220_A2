from deliveryProblemSolvingAgentClass import deliveryProblemSolvingAgent
from visualGraph import drawGraph
class deliveryProblemSolvingAgentPro(deliveryProblemSolvingAgent):



  def search(self, problem):
     seq, steps, allNodeColors = self.program(problem)
     solution=self.actions_path(seq.path())
     return (solution, steps, allNodeColors)
  
  def run(self):
    print("goal list:", self.goal)
    if isinstance(self.goal, list) and len(self.goal)>1:
      percept=self.state
      while len(self.goal)>0:
        current_goal=self.goal[0]
        print("current percept:", percept)
        print("current goal:", current_goal)
        """Formulate a goal and problem, then search for a sequence of actions to solve it."""
        #4-phase problem-solving process
        self.state = self.update_state(self.state, percept)
        goal = current_goal
        problem = self.formulate_problem(self.state, goal)
        solution, steps, allNodeColors = self.search(problem)
        self.seq.append(solution)

       # self.seq.append(self.search(problem))
        percept=current_goal
        self.goal.remove(goal)
        print("goal list:", self.goal)

        drawGraph(self.dataGraph, allNodeColors[steps-1], steps)
      if not self.seq:
                return None
      return self.seq
    else:
      return super().__call__(self.state)




