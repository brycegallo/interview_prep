// leetcode 0217 - Contains Duplicate
// Easy - Arrays & Hashing
// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.
// Time: O(n) Memory: O(n)
// Solution using hash set
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> uniques = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (uniques.contains(nums[i])) {
                return true;
            }
            uniques.add(nums[i]);
        }
        return false;
    }
}
