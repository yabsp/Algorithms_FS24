class EagerPrim:
    def __init__(self, graph):
        self.total_weight = 0
        self.included_nodes = [False] * graph.no_nodes()
        self.edge_to = [None] * graph.no_nodes()
        self.dist_to = [float('inf')] * graph.no_nodes()
        self.pq = IndexMinPQ()

        self.dist_to[0] = 0
        self.pq.insert(0, 0)  # insert the starting node into pq with priority 0
        while not self.pq.empty():
            self.visit(graph, self.pq.del_min())

    def visit(self, graph, v):
        self.included_nodes[v] = True
        for edge in graph.incident_edge(v):
            w = edge.other_node(v)
            if self.included_nodes[w]:
                continue
            if edge.weight() < self.dist_to[w]:
                self.edge_to[w] = edge
                self.dist_to[w] = edge.weight()
                if self.pq.contains(w):
                    self.pq.change(w, edge.weight())
                else:
                    self.pq.insert(w, edge.weight())
