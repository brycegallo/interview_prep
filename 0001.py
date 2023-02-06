# leetcode 0001 - Two Sum
# Given an array of integers nums and an integer target,
#       return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
#       and you may not use the same element twice.
# You can return the answer in any order.

# Naive Solution
class NaiveSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Better Solution
class BetterSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}  # value : index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                return [hashMap[difference], i]  # hashMap[difference] will return index of that value
            hashMap[n] = i
