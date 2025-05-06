# leetcode 0063 - Unique Paths II
# Medium - 2D-DP
#
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# Time: O(n) Memory: O(n) where n for both = columns in grid
class BetterSolution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # single row in memory solution
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * columns
        dp[columns - 1] = 1

        for row in reversed(range(rows)):
            for column in reversed(range(columns)):
                if obstacleGrid[row][column]:
                    dp[column] = 0
                elif column + 1 < columns:
                    dp[column] = dp[column] + dp[column + 1]

        return dp[0]

class RecursiveSolution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(rows - 1, columns - 1): 1}  # base case, bottom right position will be 1

        def dfs(row, column):
            # if row == rows or column == columns, we have gone out of bounds
            # if obstacleGrid[row][column] we have reached an obstacle
            if row == rows or column == columns or obstacleGrid[row][column]:
                return 0  # return 0 because this is not resulting in a unique path to be added to the result
            # if (row, column) in dp, result already calculated, refer to dp hashmap
            if (row, column) in dp:
                return dp[(row, column)]  # return what is found there
            # run problem on next two open squares in grid to the right and left
            dp[(row, column)] = dfs(row + 1, column) + dfs(row, column + 1)
            return dp[(row, column)]

        return dfs(0, 0)
