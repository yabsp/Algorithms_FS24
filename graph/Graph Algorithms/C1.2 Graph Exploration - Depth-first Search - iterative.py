def depth_first_search(graph, node):
    visited = set()
    stack = deque()
    stack.append(node)
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for s in graph.successors(v):
                stack.append(s)
