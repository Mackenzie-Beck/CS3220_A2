class SimpleProblemSolvingAgentProgram:
  #Abstract framework for a problem-solving agent
  def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []#solution.
        print(self.seq)

  def __call__(self, percept):
        """Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        #4-phase problem-solving process
        #print(0)
        self.state = self.update_state(self.state, percept)
        #print(self.state)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            #print(problem.initial)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        # Modified for A*
        #print('test1',self.seq)
        #print('test2',self.seq[0])
        if self.seq and isinstance(self.seq[0], list) and self.seq[0]:    
            return self.seq[0].pop(0)
        else:
            return None
        #return self.seq.pop(0)

  def update_state(self, state, percept):
        raise NotImplementedError

  def formulate_goal(self, state):
        raise NotImplementedError

  def formulate_problem(self, state, goal):
        raise NotImplementedError

  def search(self, problem):
        raise NotImplementedError