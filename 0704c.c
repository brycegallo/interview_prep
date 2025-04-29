// Leetcode 0704 - Binary Search
// Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
// You must write an algorithm with O(log n) runtime complexity.
//
// Binary search Solution
// Time Complexity: O(log2 n) Memory: O(1)

int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    // this while-loop will eventually have to exit if the target isn't in nums
    while (left <= right) {
	// this is just left + right / 2 written in a way to prevent int overflows
	int middle = left + floor ((right - left) / 2);

	// might make things quicker to avoid some computations
	if (nums[left] == target) { return left; }
	if (nums[right] == target) { return right; }
	
	if (nums[middle] < target) {
	    left = middle + 1;
	}
	if (nums[middle] > target) {
	    right = middle - 1;
	}
	else { return middle; }
    }
    // if we exited the above while-loop, target isn't in nums so we return -1
    return -1;
}
