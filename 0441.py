# leetcode 0441 - Arranging Coins
# Easy - Binary Search
#
# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.
# Time: O(logn) Memory: O(1)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        result = 0

        while low <= high:
            middle = (low + high) // 2
            coins = (middle / 2) * (middle + 1)
            if coins > n:
                high = middle - 1
            else:
                low = middle + 1
                result = max(middle, result)

        return result

class BruteForceSolution:  # O(n)
    def arrangeCoins(self, n: int) -> int:
        i = 1
        rows = 0
        while n > 0:
            n -= i
            i += 1
            rows += 1
        if n < 0:
            rows -= 1

        return rows
