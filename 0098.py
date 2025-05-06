# leetcode 0098 - Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, lowbound, upbound):
            if node:
                if lowbound < node.val and node.val < upbound:
                    return (helper(node.left, lowbound, node.val) and
                            helper(node.right, node.val, upbound))
                return False
            return True

        return helper(root, float('-inf'), float('inf')
)
