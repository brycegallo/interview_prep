# leetcode 0200 - Number of Islands
# Medium - Graphs
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# Time: O(m*n) Memory: O(1)
class BfsSolution:  # Breadth-First Search Solution with constant memory (?) by avoiding use of "visited" set
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


class DfsSolution:  # Depth-First Search Solution with constant memory (?) by avoiding use of "visited" set
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if grid:
            rows, cols = len(grid), len(grid[0])

            def dfs(r, c):
                if (
                    r not in range(rows)
                    or c not in range(cols)
                    or grid[r][c] != "1"
                ):
                    return

                grid[r][c] = "2"
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == "1":
                        islands += 1
                        dfs(r, c)
        return islands


class OldSolution:
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