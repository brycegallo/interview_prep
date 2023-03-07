# leetcode 0054 - Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Time: O(m*n) Memory: O(1) if we don't count output as extra memory
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])  # not len(matrix[0] - 1), maybe change this
        result = []

        while left < right and top < bottom:
            # top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # right edge column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if len(result) == len(matrix[0]) * len(matrix):
                return result

            # bottom row
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # left edge column
            for i in range(bottom - 1, top -1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
