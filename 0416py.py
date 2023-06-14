# leetcode 0416 - Partition Equal Subset Sum
# Medium
#
# Given an integer array nums, return true if you can partition the array into two subsets
# such that the sum of the elements in both subsets is equal or false otherwise.

# Time: O(n * sum(nums) Memory: O(sum(nums)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        for i in reversed(range(len(nums))):
            next_dp = dp.copy()
            for target in dp:
                next_dp.add(target + nums[i])
            dp = next_dp
        return (sum(nums) // 2) in dp
