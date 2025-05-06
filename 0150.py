# leetcode 0150 - Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for character in tokens:
            if character == '+':
                stack.append(stack.pop() + stack.pop())
            elif character == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif character == '*':
                stack.append(stack.pop() * stack.pop())
            elif character == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(character))
        return stack[0]