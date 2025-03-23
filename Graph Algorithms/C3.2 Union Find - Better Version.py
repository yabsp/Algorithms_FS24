class QuickUnion:
    def __init__(self, no_nodes):
        self.components = no_nodes
        self.parent = list(range(no_nodes))

    def count(self):
        return self.components

    def find(self, v):
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def union(self, v, w):
        repr_v = self.find(v)
        repr_w = self.find(w)
        if repr_w == repr_v:
            return
        self.parent[repr_v] = repr_w
        self.components -= 1
