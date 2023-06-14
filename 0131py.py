# leetcode 0131. Palindrome Partitioning
# Medium - Backtracking
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# Time: O(2^n) Memory: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_partition = []

        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i):
            if i >= len(s):
                result.append(current_partition.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    current_partition.append(s[i:j + 1])
                    dfs(j + 1)
                    current_partition.pop()

        dfs(0)
        return result
