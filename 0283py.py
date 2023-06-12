# leetcode 0283 - Move Zeroes
# Easy
#
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Time: O(n) Memory: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != 0:
                left += 1
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            right += 1
