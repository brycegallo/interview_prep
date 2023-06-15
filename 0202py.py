# leetcode 0202 - Happy Number
# Easy - Math & Geometry
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly
#     in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.
# Time: O(n) Memory: O(n)
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def sumOfSquares(n):
            result = 0

            while n:
                digit = (n % 10) ** 2
                result += digit
                n = n // 10

            return result

        while n not in visited:
            visited.add(n)
            n = sumOfSquares(n)

            if n == 1:
                return True

        return False
