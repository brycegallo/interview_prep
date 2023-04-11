# leetcode 0704 - Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index.
# Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            half = (l + r) // 2
            # for non-python languages with bounded integers
            # half = l + ((r - l) // 2)
            if nums[half] > target:
                r = half
            elif nums[half] < target:
                l = half + 1
            elif nums[half] == target:
                return half
            else:
                return -1
        return -1
