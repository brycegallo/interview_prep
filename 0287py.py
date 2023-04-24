# leetcode 0287 - Find the Duplicate Number
# Medium
#
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
# Time: O(n) Memory: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow, slowest = 0, 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        while slowest != slow:
            slow = nums[slow]
            slowest = nums[slowest]
        return slow