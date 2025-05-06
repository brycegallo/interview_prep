# leetcode 0416 - Partition Equal Subset Sum
# Medium - 1D-DP
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
        sum_target = (sum(nums) // 2)

        for i in reversed(range(len(nums))):
            next_dp = dp.copy()
            for target in dp:
                if (target + nums[i]) == sum_target:
                    return True
                next_dp.add(target + nums[i])
            dp = next_dp
        return sum_target in dp
