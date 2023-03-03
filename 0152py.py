# leetcode 0152 - Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Time O(n), Memory O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currentMin = currentMax = 1

        for n in nums:
            tempNcMax = currentMax * n
            currentMax = max(currentMax * n, currentMin * n, n)
            currentMin = min(tempNcMax, currentMin * n, n)
            result = max(result, currentMax)

        return result
