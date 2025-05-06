# leetcode 0102 - Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        q = collections.deque()

        if root:
            q.append(root)

        while q:
            values = []
            for _ in range(len(q)):
                node = q.popleft()
                values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            results.append(values)

        return results
