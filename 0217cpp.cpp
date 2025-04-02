// leetcode 0217 - Contains Duplicate
/*** Easy - Arrays & Hashing ***/
// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.

// Sorting
// Time: O(n log n)
// Space: O(n) or O(1) depending on the sorting algorithm
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums [i - 1]) {
                return true;
            }
        }
        return false;
    }
};

// Hash Set
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};

// Hash Set Length
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();
    }
};