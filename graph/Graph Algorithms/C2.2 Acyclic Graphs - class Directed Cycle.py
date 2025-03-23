from collections import deque


class DirectedCycle:
    def __init__(self, graph):
        self.predecessor = dict()
        self.on_current_path = set()
        self.cycle = None
        for node in graph.nodes:
            if self.has_cycle():
                break
            if node not in self.predecessor:
                self.predecessor[node] = node
                self.dfs(graph, node)

    def has_cycle(self):
        return self.cycle is not None

    def dfs(self, graph, node):
        self.on_current_path.add(node)
        for s in graph.successors(node):
            if self.has_cycle():
                return
            if s in self.on_current_path:
                self.predecessor[s] = node
                self.extract_cycle(s)
            if s not in self.predecessor:
                self.predecessor[s] = node
                self.dfs(graph, s)
        self.on_current_path.remove(node)

    def extract_cycle(self, node):
        self.cycle = deque()
        current = node
        self.cycle.appendleft(current)
        while True:
            current = self.predecessor[current]
            self.cycle.appendleft(current)
            if current == node:
                return

