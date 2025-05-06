// leetcode 0019 - Remove Nth Node from End of List
// Given the head of a linked list, remove the nth node from the end of the list and return its head.
// Definition for singly-linked list.
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let newnode = new ListNode(0, head)
    let [left, right] = [newnode, head]

    while (n > 0) {
        right = right.next;
        n -= 1;
    }
    while (right !== null) {
        left = left.next;
        right = right.next;
    }
    left.next = left.next.next;
    return newnode.next;
};