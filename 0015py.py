# leetcode 0015 - 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a < 1:
                if not (i > 0 and a == nums[i-1]):
                    l, r = i+1, len(nums)-1
                    while l < r:
                        threesum = a + nums[l] + nums[r]
                        if threesum > 0:
                            r -= 1
                        elif threesum < 0:
                            l += 1
                        else:
                            result.append([a, nums[l], nums[r]])
                            l += 1
                            r -= 1
                            while nums[l] == nums[l - 1] and l < r:
                                l += 1
        return result
