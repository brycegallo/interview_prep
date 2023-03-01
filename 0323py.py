# leetcode 0323 - Number of Connected Components in an Undirected Graph
# You have a graph of n nodes. You are given an integer n and an array edges where
# edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(node):
            result = node
            while result != parents[result]:
                parents[result] = parents[parents[result]]
                result = parents[result]
            return result

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return 0
            if ranks[parent2] > ranks[parent1]:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            else:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
            return 1

        result = n
        for node1, node2 in edges:
            result -= union(node1, node2)
        return result
