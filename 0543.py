# leetcode 0543 - Diameter of Binary Tree
# Easy
#
# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
# Time: O(n) Memory: O(1) or maybe O(n) because of the stack idk
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root):
            if not root:
                return -1
            left, right = dfs(root.left), dfs(root.right)
            result[0] = max(result[0], left + right + 2)
            return 1 + max(left, right)

        dfs(root)
        return result[0]