# leetcode 0213 - House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            rob1, rob2 = 0, 0  # largest possible amount we can rob will be stored in rob2 at the end

            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
