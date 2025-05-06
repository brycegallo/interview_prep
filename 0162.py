# leetcode 0162 - Find Peak Element
# Medium - Binary Search
#
# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words,
# an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
# Time: O(logn) Memory: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = low + ((high - low) // 2)
            # check if left neighboring element is greater
            if middle > 0 and nums[middle - 1] > nums[middle]:
                high = middle - 1
            # check if right neighboring element is greater
            elif middle < len(nums) - 1 and nums[middle + 1] > nums[middle]:
                low = middle + 1
            else:
                return middle
