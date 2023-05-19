# leetcode 0047 - Permutations II
# Medium
#
# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.
# Time: O() Memory: O()
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        count = {num: 0 for num in nums}
        for n in nums:
            count[n] += 1

        def dfs_backtrack():
            if len(permutation) == len(nums):
                result.append(permutation[::])
                return

            for n in count:
                if count[n] > 0:
                    permutation.append(n)
                    count[n] -= 1

                    dfs_backtrack()

                    count[n] += 1
                    permutation.pop()

            return result

        return dfs_backtrack()
