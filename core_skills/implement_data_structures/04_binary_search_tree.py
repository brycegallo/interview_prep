# Implementation of a Binary Search Tree Map in Python
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            elif key > current.key:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
            else:
                current.value = val
                return

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return -1

    def getMin(self) -> int:
        current = self.root
        if not current:
            return -1
        while current.left:
            current = current.left
        return current.value

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        current = self.root
        if not current:
            return -1
        while current.right:
            current = current.right
        return current.value

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # remove node with specified key, return new root of subtree
    def removeHelper(self, current, key) -> TreeNode:
        if current:
            if key < current.key:
                current.left = self.removeHelper(current.left)
            elif key > current.key:
                current.right = self.removeHelper(current.right)
            else:
                if current.left == None:
                    return current.right
                elif current.right == None:
                    return current.left
                else:
                    # if there are two subtrees, swap current with inorder successor
                    min_node = self.findMin(current.right)
                    current.key = min_node.key
                    current.value = min_node.value
                    current.right = self.removeHelper(current.right, min_node.key)
        return current

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
