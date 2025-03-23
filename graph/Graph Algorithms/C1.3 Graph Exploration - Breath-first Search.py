def breath_first_exploration(graph, node):
    visited = set()
    queue = deque()
    queue.append(node)
    while queue:
        v = queue.popleft()
        for s in successors(v):
            if v not in visited:
                visited.add(v)
                queue.append(s)