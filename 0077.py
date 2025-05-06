# leetcode 0077 - Combinations
# Medium
#
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
# Time: O(k*n^k) where k is the height of the decision tree Memory: O(n)?
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, combination):
            if len(combination) == k:
                result.append(combination[::])
                return

            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

            return result

        return backtrack(1, [])
