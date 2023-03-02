# leetcode 0297 - Serialize and Deserialize Binary Tree
# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can be
# deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative
# and come up with different approaches yourself.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution of Time 2 * O(n) because serialization and deserialization will each take O(n)
# memory O(n) ?
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))  # append before recursively calling DFS because this is preorder
            dfs(node.left)
            dfs(node.right)

        # no return needed, python will return None by default here

        dfs(root)
        return ",".join(result)  # comma delimiter will add elements to string, separating with comma

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")  # creates array of elements from string, new element at each comma
        self.i = 0  # create new Class member (global) variable so nothing has to be passed into this dfs

        def dfs():
            if values[self.i] == "N":  # base case, node has no children
                self.i += 1  # iterate because we are done processing this index's value
                return None  # Null is a valid binary tree
            node = TreeNode(int(values[self.i]))
            self.i += 1  # need to update i before calling dfs because each layer needs to use next i
            node.left = dfs()  # each dfs call will return a tree, even if that tree is Null
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
