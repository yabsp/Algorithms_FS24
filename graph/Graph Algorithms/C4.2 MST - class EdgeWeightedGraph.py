class EdgeWeightedGraph:
    def __init__(self, no_nodes):
        self.nodes = no_nodes
        self.edges = 0
        self.incident = [[] for l in range(no_nodes)]

    def add_edge(self, edge):
        either = edge.either_node()
        other = edge.other_node(either)
        self.incident[either].append(edge)
        self.incident[other].append(edge)
        self.edges += 1

    def no_nodes(self):
        return self.nodes

    def no_edges(self):
        return self.edges

    def incident_edges(self, node):
        for edge in self.incident_edges(node):
            yield edge

    def all_edges(self):
        for node in range(self.nodes):
            for edge in self.incident_edges[node]:
                if edge.other_node(node) > node:
                    yield edge