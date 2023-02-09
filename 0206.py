# leetcode 0206 - Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  # iterative, optimal solution, Time O(n), Space O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            nxt = cur.next  # temporary next to avoid loss
            cur.next = prev  # set next of current node to previous node
            prev = cur  # set previous node to current node
            cur = nxt  # set current node to next node

        return prev

# recursive solution, sub-optimal, time and space both O(n)
    class RecursiveSolution:  # iterative, optimal solution, Time O(n), Space O(1)
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # define base case here, where head of the list is Null
            if not head:
                return None

            newHead = head  # head is the current head of the recursive call
            if head.next:  # if next is not null
                newHead = self.reverseList(head.next)
                head.next.next = head
            head.next = None

            return newHead
