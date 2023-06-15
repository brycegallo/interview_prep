# leetcode 0050 - Pow(x, n)
# Medium - Math & Geometry
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Time: O(n)? Memory: O(n)?
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if not x: return 0
            if not n: return 1

            result = helper(x * x, n // 2)
            return x * result if n % 2 else result

        result = helper(x, abs(n))
        return result if n >= 0 else 1 / result