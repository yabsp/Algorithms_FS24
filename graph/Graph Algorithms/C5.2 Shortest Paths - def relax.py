def relax(self, edge):
    u = edge.from_node()
    v = edge.to_node()
    if self.distance[v] > self.distance[u] + edge.weight():
        self.parent[v] = u
        self.distance[v] = self.distance[u] + edge.weight()