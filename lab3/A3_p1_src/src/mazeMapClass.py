from graphClass import Graph

class mazeMap(Graph):
    def __init__(self, graph_dict = None, locations = None):
        self.g = dict()
        super().__init__(graph_dict)
        self.make_graph()
        self.locations = locations
    
    def getLocation(self,a):
        return self.locations.get(a)
    
    #Overriden
    def make_graph(self):
        for a in self.graph_dict.keys():
            for (act, b) in self.graph_dict[a].items():
                self.connect(a, b, 1)
    def connect(self, A, B, distance):
        self.g.setdefault(A, {})[B] = distance
    def nodes(self):
        return [k for k in self.graph_dict.keys()]