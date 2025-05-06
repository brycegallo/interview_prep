// leetcode 0206 - Reverse Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// iterative
var reverseList = function(head) {
    let current = head;
    let previous = null;
    while (current !== null) {
        let next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
};

// recursive
const reverseList = (head, previous = null) => {
  if (head === null) return previous;
  let next = head.next;
  head.next = previous;
  return reverseList(next, head);
};