# leetcode 1448 - Count Good Nodes in Binary Tree
# Medium
#
# Given a binary tree root, a node X in the tree is named good
# if in the path from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
# Time: O(n) Memory: O(n) if every node has only one leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = [0]

        def dfs(root, maxval):
            if not root:
                return None
            if root.val >= maxval:
                result[0] += 1
            maxval = max(maxval, root.val)
            dfs(root.left, maxval)
            dfs(root.right, maxval)

        dfs(root, root.val)
        return result[0]