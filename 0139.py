# leetcode 0139 - Word Break
# Given a string s and a dictionary of strings wordDict, return true if s
# can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Time: O(m*n^2)  Memory: O(m) where m is the length of s
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s))
        dp.append(True)

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if not dp[i] and (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
        return dp[0]
