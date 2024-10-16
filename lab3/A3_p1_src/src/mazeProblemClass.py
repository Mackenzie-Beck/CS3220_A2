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