# leetcode 0946 - Validate Stack Sequences
# Medium - Stack
#
# Given two integer arrays pushed and popped each with distinct values,
# return true if this could have been the result of a sequence of push and pop operations on an initially empty stack,
# or false otherwise.
# Time: O(n)? Memory: O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for n in pushed:
            stack.append(n)
            while stack and i < len(popped) and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return not stack
