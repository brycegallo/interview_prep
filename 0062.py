# leetcode 0062 - Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n,
# return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
# DP Solution, Time: O(m*n), Memory: O(n), really O(2n) but we reduce
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        oldRow = [1] * n

        for row in range(m-1):
            newRow = [1] * n
            for column in range(n - 2, -1, -1):
                newRow[column] = newRow[column + 1] + oldRow[column]
            oldRow = newRow

        return oldRow[0]


# math solution, don't actually use, Time: O(1), Memory O(1)
import math


class MathSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial((m - 1) + (n - 1)) / math.factorial(m-1) / math.factorial(n-1))
