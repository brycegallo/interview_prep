# leetcode 0219 - Contains Duplicate II
# Easy
#
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.
# Time: O(n) Memory: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
