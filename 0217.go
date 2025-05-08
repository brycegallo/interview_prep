// leetcode 0217 - Contains Duplicate
// Easy
// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.

// Hash Set solution
// Time: O(n) Memory: O(n)
func containsDuplicate(nums []int) bool {
    // canonical way to create a new map:
    seen := make(map[int]bool)
    // composite literal way would be:
    // nums_map := map[int]bool{}
    for _, num := range nums {
	if seen[num] {
	    return true
	}
	seen[num] = true
    }
    return false
}
