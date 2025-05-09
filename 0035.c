// Leetcode 0035 - Search Insert Position
// Easy - Binary Search
// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
//
// You must write an algorithm with O(log n) runtime complexity.
// Binary Search Solution
// Time Complexity: O(logn), Memory: O(1)
int searchInsert(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    // will slightly optimize solution in certain edge cases, but not really necessary
    //if (nums[right] < target) { return right + 1; }
    //if (target < nums[left]) { return left; }

    while (left <= right) {
        int middle = left + ((right - left) / 2);
        if (target < nums[middle]) {
            right = middle - 1;
        }
        else if (nums[middle] < target) {
            left = middle + 1;
        }
        else {
            return middle;
        }
    }
    return left;
}
