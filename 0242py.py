# leetcode 0242 - Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Constraints
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Naive Approach O(n^2)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for j in t:
            if j not in s:
                return False
        for i in s:
            if i not in t:
                return False
        return True

# Hashmap Approach O(t+s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):  # build hashmaps, strings are same length so just use one range
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:  # iterate through hashmaps, return false if anything doesn't have a match
            if countS[c] != countT.get(c, 0):
                return False

        return True

# Python built-in single-line solution, not good for interviews
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# O(1) memory solution, probably not good time complexity
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
