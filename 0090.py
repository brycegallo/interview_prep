# Leetcode 0090 - Subsets II
# Medium
#
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Time: O(n * 2^n) Memory: O(n)?
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                result.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return result
