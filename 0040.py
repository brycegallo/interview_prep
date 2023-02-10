# leetcode 0040 - Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        def backtrack(current, i, target):
            if target == 0:
                result.append(current.copy())
            if target < 0:
                return None

            prev = -1
            for i in range(len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtrack(current, i+1, target-candidates[i])
                current.pop()
                prev = candidates[i]
        backtrack([], 0, target)
        return result

# alternative solution
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def helper(i, current, target):
            if not target:
                result.append(current.copy())
                return None
            if i == len(candidates) or target < 0:
                return None

            helper(i+1, current + [candidates[i]], target - candidates[i])

            while i+1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            helper(i+1, current, target)

        helper(0, [], target)
        return result
