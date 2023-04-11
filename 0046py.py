# leetcode 0046 - Permutations
# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:  # base case, we have removed all elements but one from input array
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result
