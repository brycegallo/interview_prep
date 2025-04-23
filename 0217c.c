// leetcode 0217: contains duplicate

// Brute force, passes 65/77 testcases on leetcode, fails 66th due to limit exceeded
// Time Complexity: O(n^2) Space Complexity: O(1)
bool containsDuplicate(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
	for (int j = i + 1; j < numsSize; j++) {
	    if (nums[i] == nums[j]) {
		return true;
	    }
	}
    }
    return false;
}

// Sort with qsort()
// Time Complexity: O(n logn) Space Complexity: O(1)
int compare (const void *a, const void *b) {
    int *value_a = a;
    int *value_b = b;
    return *value_a - *value_b;
}

bool containsDuplicate(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(nums[0]), compare);
    for (int i = 0; i < numsSize - 1; i++) {
	if (nums[i] == nums[i + 1]) {
	    return true;
	}
    }
    return false;
}
