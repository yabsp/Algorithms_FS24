from collections import deque, defaultdict

# Define a simple graph class
class SimpleGraph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node)

    def successors(self, node):
        return self.edges[node]

# Initialize a graph
graph = SimpleGraph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'G')

# Define the lists to store the order of nodes
preorder = []
postorder = []
reverse_postorder = deque()

# Define the depth_first_exploration function
def depth_first_exploration(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return

    preorder.append(node)
    visited.add(node)
    for s in graph.successors(node):
        depth_first_exploration(graph, s, visited)
    postorder.append(node)
    reverse_postorder.appendleft(node)

# Run the depth_first_exploration function
depth_first_exploration(graph, 'A')

# Print the results
print("Preorder:", preorder)
print("Postorder:", postorder)
print("Reverse Postorder:", list(reverse_postorder))
