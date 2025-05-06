# leetcode 1929 - Concatenation of Array
# Easy
#
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i]
# and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.
# Time: O(n) Memory: O(1) unless we count the extra space for the result as memory, in which chase O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            nums.append(nums[i])
        return nums
