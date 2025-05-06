# leetcode 0680 - Valid Palindrome II
# Easy
#
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Time: O(n) Memory: O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.helper(s, left + 1, right) or self.helper(s, left, right - 1)
        return True

    def helper(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

class FailedSolution:
    def validPalindrome(self, s: str) -> bool:
        one = False
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right] and one:
                return False
            if s[left] != s[right] and not one:
                one = True
                if s[left + 1] == s[right]:
                    left += 1
                elif s[left] == s[right - 1]:
                    right -= 1
                else:
                    return False
                continue
            left += 1
            right -= 1
        return True