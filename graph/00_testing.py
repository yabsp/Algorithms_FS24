class DijkstraSSSP:
    def __init__(self, graph, start_node):
        pq = IndexMinPQ()
        self.edge_to = [None] * graph.no_nodes()
        self.distance = [float('inf')] * graph.no_nodes()

        self.distance[start_node] = 0
        pq.insert(start_node, 0)

        while not pq.empty():
            self.relax(graph, pq.del__min(), pq)


    def relax(self, graph, v, pq):
        for edge in graph.outgoing_edges(v):
            w = edge.to_node()
            if self.distance[v] + edge.weight() < self.distance[w]:
                self.distance[w] = self.distance[v] + edge.weight()
                self.edge_to[w] = edge
                if pq.contains(w):
                    pq.change(w, self.distance[w])
                else:
                    pq.insert(w, self.distance[w])