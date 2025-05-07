// Leetcode 0094 - Binary Tree Inorder Traversal
// Easy - Binary Trees
// Given the root of a binary tree, return the inorder traversal of its nodes' values
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// Recursive Solution
// Time Complexity: O(n), Memory: O(n)
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    if(root){
        int *left_array, *right_array;
        int left_size = 0, right_size = 0;
        
        if(root->left){
            left_array = inorderTraversal(root->left, &left_size);
        }
        if(root->right){
            right_array = inorderTraversal(root->right, &right_size);
        }
        *returnSize = 1 + left_size + right_size;
        
        int *result = (int*)malloc((*returnSize) * sizeof(int));
        
        int result_index = 0;
        for(int i=0; i<left_size; i++, result_index++){
            result[result_index] = left_array[i];
        }
        result[result_index++] = root->val;
        for(int i=0; i<right_size; i++, result_index++){
            result[result_index] = right_array[i];
        }
        return result;
    }
    *returnSize = 0;
    return NULL;
}
