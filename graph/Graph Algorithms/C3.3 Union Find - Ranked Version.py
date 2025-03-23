class RankedQuickUnion:
    def __init__(self, no_nodes):
        self.parent = list(range(no_nodes))
        self.components = no_nodes
        self.rank = [0] * no_nodes

    def count(self):
        return self.components

    def find(self, v):
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def union(self, v, w):
        repr_v = self.find(v)
        repr_w = self.find(w)
        if repr_v == repr_w:
            return
        if self.rank[repr_w] < self.rank[repr_v]:
            self.parent[repr_w] = repr_v
        else:
            self.parent[repr_v] = repr_w
            if self.rank[repr_v] == self.rank[repr_w]:
                self.rank[repr_w] += 1
        self.components -= 1