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