# leetcode 0169 - Majority Element
# Easy
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
# Time: O(n) Memory: O(1)
class Solution:  # Boyer-Moore algorithm
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0

        for num in nums:
            if count == 0:
                result = num
            count += (1 if num == result else -1)

        return result


# Time: O(n) Memory: O(n)
class LinearSpaceSolution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        half = len(nums) // 2

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            if hashmap[num] > half:
                return num