# leetcode 1984 - Minimum Difference Between Highest and Lowest of K Scores
# Easy
#
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
# You are also given an integer k.
# Pick the scores of any k students from the array
# so that the difference between the highest and the lowest of the k scores is minimized.
#
# Return the minimum possible difference.
# Time: O(n) Memory: O(1)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        left, right = 0, k - 1
        result = float("inf")
        nums.sort()

        while right < len(nums):
            result = min(result, nums[right] - nums[left])
            left += 1
            right += 1
        return result