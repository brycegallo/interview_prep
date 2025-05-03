# Implementation of a Singly-Linked List in Python
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Placeholder node for handling edge cases
        self.head = ListNode(-1)
        self.tail = self.head
        
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.value
            current = current.next
            i += 1
        return -1 # index out of bounds
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # check if list was empty before insertion
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        
    def remove(self, index: int) -> bool:
        current = self.head
        i = 0
        # this loop will move current to node before target node
        while i < index and current:
            i += 1
            current = current.next

        # if we have found the right node
        if current and current.next:
            # handle edge case where we're removing tail
            if current.next == self.tail:
                self.tail = current
            # dereference the target node from the list
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result
        

