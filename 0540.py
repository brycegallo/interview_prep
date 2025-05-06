# leetcode 0540 - Single Element in a Sorted Array
# Medium - Binary Search
#
# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
# Time: O(logn) Memory: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = low + ((high - low) // 2)
            if ((middle - 1 < 0 or nums[middle - 1] != nums[middle]) and
                    (middle + 1 == len(nums) or nums[middle] != nums[middle + 1])):
                return nums[middle]

            leftSize = (middle - 1) if nums[middle - 1] == nums[middle] else middle
            if leftSize % 2:
                high = middle - 1
            else:
                low = middle + 1
