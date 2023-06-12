# leetcode 0682 - Baseball Game
# Easy
#
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game,
# you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record
# and is one of the following:
#     An integer x. - Record a new score of x.
#     '+'. - Record a new score that is the sum of the previous two scores.
#     'D'. - Record a new score that is the double of the previous score.
#     'C'. - Invalidate the previous score, removing it from the record.
#
# Return the sum of all the scores on the record after applying all the operations.
#
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer
# and that all operations are valid.
# Time: O(n) Memory: O(n)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for operation in operations:
            if operation == '+':
                score_stack.append(score_stack[-1] + score_stack[-2])
            elif operation == 'D':
                score_stack.append(score_stack[-1] * 2)
            elif operation == 'C':
                score_stack.pop()
            else:
                score_stack.append(int(operation))

        return sum(score_stack)
