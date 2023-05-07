# leetcode 0014 - Longest Common Prefix
# Easy
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Time: O(n) Memory: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
