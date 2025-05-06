# leetcode 0045 - Jump Game II
# Medium
#
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#     0 <= j <= nums[i] and
#     i + j < n
#
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].
# Time: O(n) Memory: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        left = right = 0

        while right < len(nums) - 1:
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            left = right + 1
            right = furthest
            result += 1
        return result
