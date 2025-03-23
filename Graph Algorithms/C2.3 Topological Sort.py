from collections import deque


def topological_sort(acyclic_digraph):
    reverse_postorder = set()
    visited = [False] * acyclic_digraph.no_nodes()
    in_postorder = [False] * acyclic_digraph.no_nodes()
    for node in range(acyclic_digraph.no_nodes()):
        dfs(acyclic_digraph, node, visited, in_postorder, reverse_postorder)


def dfs(acyclic_digraph, node, visited, in_postorder, reverse_postorder):
    if visited[node]:
        return
    for s in acyclic_digraph.successors(node):
        dfs(acyclic_digraph, node, visited, in_postorder, reverse_postorder)
    if not in_postorder[node]:
        reverse_postorder.appendleft(node)
        in_postorder[node] = True
