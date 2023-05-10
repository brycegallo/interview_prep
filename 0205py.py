# leetcode 0205 - Isomorphic Strings
# Easy
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
# Time: O(n) Memory: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c_s, c_t = s[i], t[i]
            if (c_s in mapST and mapST[c_s] != c_t) or (c_t in mapTS and mapTS[c_t] != c_s):
                return False
            mapST[c_s] = c_t
            mapTS[c_t] = c_s
        return True
