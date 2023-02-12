# leetcode 0020 - Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')':"(",']':'[','}':'{'}

        for i in s:
            if i in hashMap:
                if stack and stack[-1] == hashMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
