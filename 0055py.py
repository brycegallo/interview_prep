# leetcode 0055 - Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            goal = i if i + nums[i] >= goal else goal
        return goal == 0
