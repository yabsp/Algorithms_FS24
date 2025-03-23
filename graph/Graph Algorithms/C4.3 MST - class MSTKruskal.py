class MSTKruskal:
    def __init__(self, graph):
        self.included_edges = []
        self.total_weight = 0

        candidates = minPQ()
        uf = UnionFind(graph.no_nodes())

        for edge in graph.all_edges():
            candidates.insert(edge)

        while (not candidates.empty() and
        len(self.included_edges) < graph.no_nodes() - 1):
            edge = candidates.del_min()
            v = edge.either_node()
            w = edge.other_node(v)
            if uf.connected(v, w):
                continue
            uf.union(v, w)
            self.included_edges.append(edge)
            self.total_weight += edge.weight()
