# leetcode 0261 - Graph Valid Tree
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
#
# Return true if the edges of the given graph make up a valid tree, and false otherwise.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {i: [] for i in range(n)}
        visited = set()

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def dfs(node, previous):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor != previous:
                    if not dfs(neighbor, node):
                        return False
            return True

        return dfs(0, -1) and n == len(visited)
