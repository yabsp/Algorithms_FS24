class LazyPrim:
    def __init__(self, graph):
        self.included_edges = []
        self.total_weight = 0

        candidates = minPQ()
        included_nodes = [False] * graph.no_nodes()

        included_nodes[0] = True
        for edge in graph.incident_edges(0):
            candidates.insert(edge)

        while (len(self.included_edges) < graph.no_nodes - 1 and (not candidates.empty())):
            edge = candidates.del_min()
            v = edge.either_edge()
            w = edge.other_node(v)
            if included_nodes[v] and included_nodes[w]:
                continue
            if included_nodes[w]:
                v, w = w, v
            included_nodes[w] = True
            self.included_edges.append(edge)
            self.total_weight += edge.weight()

            for incident in graph.incident_edges(w):
                if not included_nodes[incident.other_node(w)]:
                    candidates.insert(incident)
