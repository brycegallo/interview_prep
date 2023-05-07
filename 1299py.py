# leetcode 1299 - Replace Elements with Greatest Element on Right Side
# Easy
#
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
# Time: O(n) Memory: O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_greatest = -1
        for i in range((len(arr) - 1), -1, -1):
            new_greatest = max(right_greatest, arr[i])
            arr[i], right_greatest = right_greatest, new_greatest
        return arr
