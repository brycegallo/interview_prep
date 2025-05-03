// Leetcode 0141 - Linked List Cycle
// Given head, the head of a linked list, determine if the linked list has a cycle in it.
//
// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
//
// Return true if there is a cycle in the linked list. Otherwise, return false. 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Tortoise and Hare Solution
// Time Complexity: O(n) Memory: O(1)
// time complexity is O(n) because the hare pointer will always meet the tortoise pointer at the nth position in the linked list
bool hasCycle(struct ListNode *head) {
    if (head && head->next) {
        struct ListNode *tortoise = head;
        struct ListNode *hare = head->next;
        while (tortoise && hare && hare->next) {
            if (tortoise == hare) {
                return true;
            }
            tortoise = tortoise->next;
            hare = hare->next->next;
        }
    }
    return false;
}
