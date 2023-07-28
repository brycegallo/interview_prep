# leetcode 1071 - Greatest Common Divisor of Strings
# Easy - Math and Geometry
#
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# Time: O( min(m,n)*(m+n) ) Memory: O(1)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(length):
            if len1 % length or len2 % length:
                return False
            f1, f2 = len1 // length, len2 // length
            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for leng in range(min(len1, len2), 0, -1):
            if isDivisor(leng):
                return str1[:leng]
        return ""
