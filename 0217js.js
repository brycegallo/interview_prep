// leetcode 0217 - Contains Duplicate
// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = (nums, numSet = new Set()) => {
    for (const n of nums) {
        if (numSet.has(n)) return true;

        numSet.add(n);
    }
    return false;
};