#Implementation of a Double-ended Queue in Python

# Doubly-Linked List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

# Every method in the class has a time complexity of O(1)
# This is thanks to us using pointer manipulation for each one
class Deque:
    def __init__(self):
        # create two placeholder nodes
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.previous = self.left

    def isEmpty(self) -> bool:
        # if there are no nodes between placeholders, deque is empty
        return self.left.next == self.right

    def append(self, value: int) -> None:
        last_node = self.right.previous
        new_node = Node(value)

        last_node.next = new_node
        new_node.previous = last_node

        new_node.next = self.right
        self.right.previous = new_node


    def appendleft(self, value: int) -> None:
        first_node = self.left.next
        new_node = Node(value)

        first_node.previous = new_node
        new_node.next = first_node

        new_node.previous = self.left
        self.left.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.right.previous
        value = last_node.value
        new_last_node = last_node.previous

        new_last_node.next = self.right
        self.right.previous = new_last_node

        return value

        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.left.next
        value = first_node.value
        new_first_node = first_node.next

        new_first_node.previous = self.left
        self.left.next = new_first_node

        return value

