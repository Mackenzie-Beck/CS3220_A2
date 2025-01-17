from graphClass import Graph

class mazeMap(Graph):
    def __init__(self, graph_dict = None, locations = None):
        self.g = dict()
        super().__init__(graph_dict)
        self.make_graph()
        self.locations = locations
    
    def getLocation(self,a):
        return self.locations.get(a)
    
    def make_graph(self):
        for a in self.graph_dict.keys():
            for (act, b) in self.graph_dict[a].items():
                self.connect(a, b, 1)

    def connect(self, A, B, distance):
        self.g.setdefault(A, {})[B] = distance

    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([v2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
    
    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.g.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)