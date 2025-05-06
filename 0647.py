# leetcode 0647 - Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# Time O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = [0]

        def helper(even):
            for i in range(len(s)):
                left, r = i, i + even
                while left >= 0 and r < len(s) and s[left] == s[r]:
                    result[0] += 1
                    left -= 1
                    r += 1

        helper(0)
        helper(1)
        return result[0]