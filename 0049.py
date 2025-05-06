# leetcode 0049 - Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # mapping character count to list of groupAnagrams, defaultdict avoids edge case
        for s in strs:
            count = [0] * 26  # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)
        return result.values()