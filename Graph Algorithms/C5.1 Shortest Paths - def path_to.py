def path_to(self, node):
    if self.distance[node] == float('inf'):
        yield None
    elif self.parent[node] is None:
        yield node
    else:
        self.path_to(self.parent[node])
        yield node