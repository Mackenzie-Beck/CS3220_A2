from problemClass import Problem

class MazeProblem(Problem):

    '''
    The state space is stored as nested dictionaries
    G={state1:{action1:state2, action2: state N..},
       .....}

    '''
    def __init__(self, initial, goal, graph):
      super().__init__(initial, goal)
      self.graph = graph#The state space -instance of vacuumGraph Class

    def actions(self, A):
      return list(self.graph.graph_dict[A].keys())
      #return list(self.graph.get(A).keys())

    def result(self, state, action):
      #A transition model
      return self.graph.graph_dict[state][action]
      #return self.graph.get(state).get(action)

    def path_cost(self, cost_so_far, A, action, B):
        action_costs = {
            'left': 1,
            'right': 1,
            'up': 1,
            'down': 1
        }
        return cost_so_far + action_costs[action]
