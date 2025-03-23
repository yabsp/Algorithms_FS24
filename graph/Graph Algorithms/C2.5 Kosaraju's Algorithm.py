from collections import deque, defaultdict

# Define the depth_first_exploration function for reverse postorder
def depth_first_exploration(graph, node, visited, order):
    stack = deque([node])
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            order.appendleft(current)  # Preorder: Add before traversing successors
            for successor in graph.successors(current):
                if successor not in visited:
                    stack.append(successor)
    return order

# Compute strongly connected components using Kosaraju's algorithm
def compute_strongly_connected_components(directed_graph):
    # Step 1: Create a reversed graph
    reversed_graph = directed_graph.reverse()

    # Step 2: Compute reverse postorder for reversed graph
    visited = set()
    reverse_postorder = deque()
    for node in reversed_graph.nodes:
        if node not in visited:
            depth_first_exploration(reversed_graph, node, visited, reverse_postorder)

    print("Reverse Postorder:", list(reverse_postorder))  # Print reverse postorder for debugging

    # Step 3: Determine the strongly connected components
    visited = set()
    sccs = []  # List to store SCCs
    for node in reverse_postorder:
        if node not in visited:
            scc = deque()
            depth_first_exploration(directed_graph, node, visited, scc)
            sccs.append(list(scc))  # Convert deque to list for easier reading

    return sccs

# Example usage
class SimpleGraph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node)

    def successors(self, node):
        return self.edges[node]

    def reverse(self):
        reversed_graph = SimpleGraph()
        for from_node in self.edges:
            for to_node in self.edges[from_node]:
                reversed_graph.add_edge(to_node, from_node)
        return reversed_graph

    @property
    def nodes(self):
        return set(self.edges.keys()).union(*self.edges.values())

# Create a directed graph
graph = SimpleGraph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')
graph.add_edge('F', 'D')
graph.add_edge('G', 'F')
graph.add_edge('G', 'H')
graph.add_edge('H', 'I')
graph.add_edge('I', 'J')
graph.add_edge('J', 'G')

# Compute strongly connected components
sccs = compute_strongly_connected_components(graph)
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
