def shortest_path(graph, from_node, to_node):
    predecessor = bfs_with_predecessors(graph, from_node)
    if to_node not in predecessor:
        print("There is no path from " + from_node + " to " + to_node)
        return None
    path = deque()
    current_node = to_node
    pre = predecessor[current_node]
    while pre is not current_node:
        path.appendleft((pre, current_node))
        current_node = pre
        pre = predecessor[current_node]
    return path

