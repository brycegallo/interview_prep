# leetcode 0066 - Plus One
# Easy - Math & Geometry
#
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
# Time: O(n) Memory: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in reversed(range(len(digits))):
            if carry:
                digits[i] += 1
                carry = 0
            if digits[i] > 9:
                digits[i] = 0
                carry = 1

        if carry and not digits[0]:
            digits.insert(0, 1)

        return digits
