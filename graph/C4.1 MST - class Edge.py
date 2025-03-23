class Edge:
    def __init__(self, n1, n2, weight):
        self.n1 = n1
        self.n2 = n2
        self.edge_weight = weight

    def weight(self):
        return self.edge_weight

    def either_node(self):
        return self.n1

    def other_node(self, n):
        if self.n1 == n:
            return self.n1
        return self.n2
    