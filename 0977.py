# leetcode 0977 - Squares of a Sorted Array
# Easy - Two Pointer(?)
#
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# Time: O(n) Memory: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        last = -1
        result = [0] * len(nums)

        while left <= right:
            if abs(nums[left]) < nums[right]:
                result[last] = (nums[right] ** 2)
                right -= 1
            else:
                result[last] = (nums[left] ** 2)
                left += 1
            last -= 1
        return result
