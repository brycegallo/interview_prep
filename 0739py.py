# leetcode 0739 - Daily Temperatures
# Medium

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day
# to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# Time O(n), Memory O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        return result
