# leetcode 1207 - Unique Number of Occurrences
# Easy
#
# Given an array of integers arr, return true if the number of occurrences of each value
# in the array is unique or false otherwise.
# Time: O(n) Memory: O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_hashmap = {}
        my_set = set()

        for num in arr:
            if num in my_hashmap:
                my_hashmap[num] += 1
            else:
                my_hashmap[num] = 1

        for value in my_hashmap.values():
            if value in my_set:
                return False
            else:
                my_set.add(value)

        return True