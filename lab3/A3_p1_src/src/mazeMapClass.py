from graphClass import Graph

class mazeMap(Graph):
    def __init__(self, graph_dict = None, locations = None):
        super().__init__(graph_dict)
        self.locations = locations
    
    def getLocation(self,a):
        return self.locations.get(a)
    
    #Overrides
    def make_graph(self):
        for a in list(self.graph_dict.keys()):
            for (b, direction) in self.graph_dict[a].items():
                self.connect(b, a, direction)
    def connect(self, A, B, direction):
        if direction == 'North': direction = 'South'
        elif direction == 'South': direction = 'North'
        elif direction == 'East': direction = 'West'
        elif direction == 'West': direction = 'East'
        self.graph_dict.setdefault(A, {})[B] = direction