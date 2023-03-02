# leetcode 0005 - Longest Palindromic Substring
# Given a string s, return the longest palindromic substringin s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = [""]

        def helper(even):
            for i in range(len(s)):
                left, r = i, i + even
                while left >= 0 and r < len(s) and s[left] == s[r]:
                    if (r - left + 1) > len(result[0]):
                        result[0] = s[left: r + 1]
                    left -= 1
                    r += 1

        helper(0)
        helper(1)
        return result[0]
