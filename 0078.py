# leetcode 0078 - Subsets
# Given an integer array nums of unique elements, return all possible
# subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):  # base case: if we go beyond bounds of nums array
                result.append(subset.copy())
                return

            subset.append(nums[i])  # decision to include i in subset
            dfs(i + 1)

            subset.pop()  # decision not to include i in subset
            dfs(i + 1)

        dfs(0)
        return result

