// Leetcode 0206 - Reverse Linked List
// Easy - Linked Lists
// Given the head of a singly linked list, reverse the list, and return the reversed list
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Optimal Solution: Two pointer solution, iterative 
// Time Complexity: O(n), Memory: O(1)
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* current = head;
    // previous and placeholder must be NULL to avoid retaining their values from prior leetcode testcases
    struct ListNode* previous = NULL;
    struct ListNode* placeholder = NULL;
}

// Sub-optimal Solution: Recursive solution
// Time Complexity: O(n), Memory: O(n)
struct ListNode* recursiveReverseList(struct ListNode* head) {
    if (!head) {
	return NULL;
    }
    struct ListNode* new_head = head;
    if (head->next) {
	new_head = recursiveReverseList(head->next);
	head->next->next = head;
    }
    head->next = NULL;
    return new_head;
}
