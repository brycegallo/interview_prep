# leetcode 0118 - Pascal's Triangle
# Easy
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Time: O(n^2) Memory: O(n)?
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows - 1):
            temp_row = [0] + result[-1] + [0]
            new_row = []
            for j in range(len(result[-1]) + 1):
                new_row.append(temp_row[j] + temp_row[j+1])
            result.append(new_row)
        return result
