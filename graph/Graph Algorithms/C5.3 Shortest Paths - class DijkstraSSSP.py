class DijkstraSSSP:
    def __init__(self, graph, start_node):
        self.edge_to = [None] * graph.no_nodes()
        pq = IndexMinPQ()
        self.distance = [float('inf')] * graph.no_nodes

        self.distance[start_node] = 0
        pq.insert(start_node, 0)

        while not pq.empty():
            self.relax(graph, pq.del_min(), pq)

    def relax(self, graph, v, pq):
        for edge in graph.outgoing_edges():
            w = edge.to_node()
            if self.distance[v] + edge.weight() < self.distance[w]:
                self.edge_to[w] = edge
                self.distance[w] = self.distance[v] + edge.weight()
                if pq.contains(w):
                    pq.change(w, self.distance[w])
                else:
                    pq.insert(w, self.distance[w])