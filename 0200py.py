# leetcode 0242 - Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if grid:
            rows, columns = len(grid), len(grid[0])

            def bfs(row, column):
                q = deque()
                q.append((row, column))

                while q:
                    q_row, q_column = q.popleft()
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                    for d_row, d_column in directions:
                        row, column = q_row + d_row, q_column + d_column
                        if (row) in range(rows) and (column) in range(columns) and grid[row][column] == '1':
                            q.append((row, column))
                            grid[row][column] = "2"

            for row in range(rows):
                for column in range(columns):
                    if grid[row][column] == "1":
                        grid[row][column] = "2"
                        bfs(row, column)
                        islands += 1

        return islands