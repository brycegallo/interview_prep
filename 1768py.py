# leetcode 1768 - Merge Strings Alternately
# Easy - Two Pointers
#
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto the end of
# the merged string.
#
# Return the merged string.
# Time: O(m+n) Memory: O(m+n)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer_1 = 0
        pointer_2 = 0
        result = []

        while pointer_1 < len(word1) and pointer_2 < len(word2):
            result.append(word1[pointer_1])
            result.append(word2[pointer_2])
            pointer_1 += 1
            pointer_2 += 1
        result.append(word1[pointer_1:])
        result.append(word2[pointer_2:])
        return "".join(result)
