# leetcode 0217 - Contains Duplicate
# Easy - Arrays & Hashing
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Solution using sorting
class SortingSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return True
        return False

# Hash Set solution
# Time: O(n) Memory: O(n)
class HashSetSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
