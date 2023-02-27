# leetcode 0074 - Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
#     Each row is sorted in non-decreasing order.
#     The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        row, top, bottom = 0, 0, rows - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        if top <= bottom:
            left, right = 0, columns - 1
            while left <= right:
                mid = (left + right) // 2
                if target < matrix[row][mid]:
                    right = mid - 1
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    return True

        return False
