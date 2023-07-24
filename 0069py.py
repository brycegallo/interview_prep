# leetcode 069 - Sqrt(x)
# Easy - Binary Search
#
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Time: O(logn) Memory: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        result = 0
        while low <= high:
            middle = low + ((high - low) // 2)
            potential = middle ** 2
            if potential > x:
                high = middle -1
            elif potential < x:
                low = middle + 1
                result = middle
            else:
                return middle
        return result

class MyFirstSolution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        while low <= high:
            middle = (low + high) // 2
            potential = middle ** 2
            if potential > x:
                high = middle -1
            elif potential < x:
                low = middle + 1
            elif potential == x:
                return middle
        return low - 1