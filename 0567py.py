# leetcode
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or len(s1) > len(s2): return False
        countS1, window = {}, {}

        for char in s1:
            countS1[char] = 1 + countS1.get(char, 0)

        have, need = 0, len(countS1)
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            window[char] = 1 + window.get(char, 0)
            if char in countS1 and countS1[char] == window[char]:
                have += 1
            if need == have:
                return True
            if right >= sum(countS1.values()) - 1:
                char = s2[left]
                window[char] -= 1
                if char in countS1 and window[char] - countS1[char] == -1:
                    have -= 1
                left += 1

        return False
