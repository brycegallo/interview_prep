# leetcode 0695 - Max Area of Island
# Medium - Graphs
#
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.
# Time: O(m*n) Memory: O(1)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        largest_area = 0

        def dfs(r, c):
            if (
                    r not in range(rows)
                    or c not in range(columns)
                    or grid[r][c] != 1
            ):
                return 0

            grid[r][c] = 2
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        for row in range(rows):
            for column in range(columns):
                largest_area = max(largest_area, dfs(row, column))

        return largest_area
