# leetcode 0073 - Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# Time: O(m*n) Memory: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, columns = len(matrix), len(matrix[0])
        rowZero = False

        # first pass, find zeros and mark rows, columns for zero placement
        for row in range(rows):
            for column in range(columns):
                if not matrix[row][column]:
                    matrix[0][column] = 0  # set top column to zero, because we no longer need to check it for marking
                    if row:
                        matrix[row][0] = 0  # set leftmost column to zero, we no longer need to check it
                    else:
                        rowZero = True

        for row in range(1, rows):
            for column in range(1, columns):
                if not matrix[0][column] or not matrix[row][0]:
                    matrix[row][column] = 0

        if not matrix[0][0]:
            for row in range(rows):
                matrix[row][0] = 0

        if rowZero:
            for column in range(columns):
                matrix[0][column] = 0
