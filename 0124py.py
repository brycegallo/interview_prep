# leetcode 0124 - Binary Tree Maximum Path Sum
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has
# an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with global variable solution, Time: O(n) Memory: O(n)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)

            result[0] = max(result[0], root.val + leftmax + rightmax)
            return root.val + max(leftmax, rightmax)

        dfs(root)
        return result[0]


# DFS without global, same time and space
class nonGlobalSolution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, float("-inf")

            left, wl = dfs(root.left)
            left = max(left, 0)

            right, wr = dfs(root.right)
            right = max(right, 0)

            res = max(wl, wr, root.val + left + right)
            return root.val + max(left, right), res

        return dfs(root)[1]