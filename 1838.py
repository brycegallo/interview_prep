# leetcode 1838 - Frequency of the Most Frequent Element
# Medium - Sliding Window
#
# The frequency of an element is the number of times it occurs in an array.
#
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums
# and increment the element at that index by 1.
#
# Return the maximum possible frequency of an element after performing at most k operations.
# Time: O(nlogn) Memory: O(1)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # O(nlogn), otherwise whole function is O(n)

        left, right = 0, 0
        result, total = 0, 0

        while right < len(nums):
            total += nums[right]

            while (nums[right] * (right - left + 1)) > k + total:
                total -= nums[left]
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result
