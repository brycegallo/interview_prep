# leetcode 0424 - Longest Repeating Character Replacement
# You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get
# after performing the above operations.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, maxf, result = 0, 0, 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


class SubOptimalStandardSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, result = 0, 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
