# leetcode 0572 - Subtree of Another Tree
# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot
# and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(self, root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (sameTree(self, root.left, subRoot.left) and
                        sameTree(self, root.right, subRoot.right))
            return False

        if not root:
            return False if subRoot else True
        if sameTree(self, root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


class FirsAttempt:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (sameTree(self, root.left, subRoot.left) and
                        sameTree(self, root.right, subRoot.right))
            return False

        # order of these is important
        # if not subRoot: return True
        # if not root: return False
        # is below equivalent to above ? no
        if not root:
            return False if subRoot else True

        if root.val != subRoot.val:
            return (self.isSubtree(root.left, subRoot) or
                    self.isSubtree(root.right, subRoot))
        if root.val == subRoot.val:
            return sameTree(self, root, subRoot)


