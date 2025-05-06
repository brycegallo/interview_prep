# leetcode 0110 - Balanced Binary Tree
# Easy
#
# Given a binary tree, determine if it is height-balanced.
# Time: O(n) Memory: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, -1]
            left, right = dfs(root.left), dfs(root.right)
            balance = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return [balance, (1 + max(left[1], right[1]))]

        return dfs(root)[0]