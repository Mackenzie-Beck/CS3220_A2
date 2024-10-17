from problemClass import Problem

class MazeProblem(Problem):
    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph #The state space
    
    def actions(self, A):
        return list(self.graph.graph_dict[A].keys())
        #return list(self.graph.get(A).keys())
    
    def result(self, state, action):
        #A transition model
        #return action
        if self.graph.graph_dict[state].setdefault(action, None) == None:
            self.graph.graph_dict[state].pop(action)
            return None
        else:
            return self.graph.graph_dict[state][action]
        #return self.graph.get(state).get(action)
    
    def path_cost(self, cost_so_far, A, action, B):
        #An action cost function
        #return cost_so_far + self.result(A, action)
        return cost_so_far + self.graph.get(A, B)
    
    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return self.goal.count(state)>0
        else:
            return state == self.goal