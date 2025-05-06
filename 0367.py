# leetcode 0367 - Valid Perfect Square
# Easy - Binary Search
#
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer.
# In other words, it is the product of some integer with itself.
#
# You must not use any built-in library function, such as sqrt.
# Time: O(logn) Memory: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            middle = (low + high) // 2
            potential = middle ** 2
            if potential > num:
                high = middle - 1
            elif potential < num:
                low = middle + 1
            else:
                return True

        return False
