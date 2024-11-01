from mazeProblemSolvingAgentClass import MazeProblemSolvingAgent
import collections
from manhattanDistance import manhattanDistance

class MazeProblemSolvingAgentPro(MazeProblemSolvingAgent):
  def __init__(self, initial_state=None, dataGraph=None, goal=None, program=None):
    super().__init__(initial_state,dataGraph,goal)

    if program is None or not isinstance(program, collections.abc.Callable):
      print("Can't find a valid program for {}, falling back to default.".format(self.__class__.__name__))

      def program(percept):
        return eval(input('Percept={}; action? '.format(percept)))

    self.program = program

  def search(self, problem):
    seq = self.program(problem)
    print(seq)
    if seq is not None:
        solution = self.actions_path(seq.path())
        print("Solution (a sequence of actions) from the initial state to a goal: {}".format(solution))
        return solution, seq.path()
    else:
        print("No sequence found.")
        return [], []

  
  def actions_path(self, p):
    acts=[]
    for n in p:
      acts.append(n.action)
    return acts[1:]

  def run(self, mazeSize, ghostLocations):
    #set performance
    performance = 0.2 * mazeSize



    print("goal list:", self.goal)
    path_to_goal=[]

    if isinstance(self.goal, list) and len(self.goal)>1:
      percept=self.state
      while len(self.goal)>0:
        

       


        # get the last goal
        if len(self.goal)==1:
          current_goal = self.goal[0]
        #get every goal except the last one
        else:
          current_goal=self.optimizefood(percept, self.goal[0:-1])


        print("current percept:", percept)
        print("current goal:", current_goal)
        """Formulate a goal and problem, then search for a sequence of actions to solve it."""


        #4-phase problem-solving process
        self.state = self.update_state(self.state, percept)
        goal = current_goal
        problem = self.formulate_problem(self.state, goal)
        self.seq.append (self.search(problem)[0])
        path_to_goal.append(self.search(problem)[1])
        percept=current_goal
        self.goal.remove(goal)
        print("goal list:", self.goal)
        performance *= 2
        print("performance:", performance)



        for path in path_to_goal:
          for node in path:
            if node.state in ghostLocations:
              print("Ghost found at:", node.state)
              if performance > 0.3 * mazeSize:
                performance -= 0.1 * performance
                ghostLocations.remove(node.state)
                print("Removed ghost: ", node.state)
                print("performance:", performance)
              else:
                # Agent dies
                print("Agent dies")
                return [], []
          
      

      return self.seq, path_to_goal
    else:
        return super().__call__(self.state) 


  def optimizefood(self, currentState, foodLocations):
    return min(foodLocations, key=lambda x: manhattanDistance.calc(currentState, x))