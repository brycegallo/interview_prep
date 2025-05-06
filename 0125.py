# leetcode 0125 - Valid Palindrome
# Easy - Two Pointers
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# Constraints
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# Time: O(n) Memory: O(1)

# first attempt, with pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            print(i, -i-1)
            print(s[i], s[-i-1])
            if s.lower()[i] != s.lower()[-i-1]:
                return False
        return True

# built-in solution
# interviewers may not like this, they may not want you to use built-ins like isalnum()
# it uses extra memory when creating a new strong and reversing the old one
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# pointer solution
# not using any built-ins
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                 ord('a') <= ord(c) <= ord('z') or
                 ord('0') <= ord(c) <= ord('9'))
