def bfs_with_predecessors(graph, node):
    predecessors = [None] * graph.no_nodes()
    deque = deque()
    predecessors[node] = node
    deque.append(node)
    while queue:
        v = deque.popleft()
        for s in graph.successors(v):
            if predecessors[s] is None:
                predecessors[s] = v
                queue.append(s)
    return predecessors