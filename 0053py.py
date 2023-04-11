# leetcode 0053 - Maximum subarray
#Given an integer array nums, find the subarray with the largest sum, and return its sum.

# notes
# could do for i=0 in nums, for j=i in nums, for k=i in nums and compute value of every subarray
# but this would be incredibly wasteful

# sliding window solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            curSum *= curSum > 0  # "if curSum < 0: curSum = 0" into single line
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

