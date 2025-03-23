class QuickFind():
    def __init__(self, no_nodes):
        self.components = no_nodes
        self.representative = list(range(no_nodes))

    def count(self):
        return self.components

    def find(self, v):
        return self.representative[v]

    def union(self, v, w):
        repr_v = self.representative[v]
        repr_w = self.representative[w]
        if repr_v == repr_w:
            return
        for i in range(len(self.representative)):
            if self.representative[i] == repr_v:
                self.representative[i] = repr_w
        self.components -= 1
