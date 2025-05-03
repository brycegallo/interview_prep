// Leetcode 0021 - Merge Two Sorted Lists
// Easy - Linked List
// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Optimal Solution: Iterative
// Time Complexity: O(m+n) Memory Complexity: O(1)
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Create a placeholder node that will serve as the head of the output list
    struct  ListNode placeholder;
    placeholder.next = NULL;
    struct ListNode* place_pointer = &placeholder;

    while (list1 && list2) {
        if (list1->val <= list2->val) {
            place_pointer->next = list1;
            list1 = list1->next;
        } else {
            place_pointer->next = list2;
            list2 = list2->next;
        }
        place_pointer = place_pointer->next;
    }

    if (!list1) {
        place_pointer->next = list2;
    }
    else if (!list2) {
        place_pointer->next = list1;
    }
    return placeholder.next;
}

// Sub-optimal Solution: Recursive
// Time Complexity: O(m+n) Memory Complexity: O(m+n) i think
// might do this later
