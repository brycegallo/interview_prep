# leetcode 0136 - Single Number
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0  # n ^ 0 always = n, so here every number will xor with itself once, except one
        for n in nums:
            result = n ^ result
        return result
