# leetcde 0724 - Find Pivot Index
# Easy - Arrays & Hashing
#
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to
# the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
# Time: O(n) Memory: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        list_sum = sum(nums)  # O(n) operation
        left_sum = 0

        for i in range(len(nums)):  # O(n) loop, so overall O(2n) reduces to O(n)
            if left_sum == list_sum - nums[i] - left_sum:
                return i
            left_sum += nums[i]

        return -1
