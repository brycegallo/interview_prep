// leetcode 0217 - Contains Duplicate
// Easy
// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.

// Hash Set solution
// Time: O(n) Memory: O(n)
func containsDuplicate(nums []int) bool {
    nums_map := map[int]int{}
    for _, n := range nums {
        if _, ok := nums_map[n]; !ok {
            nums_map[n] = 1
        } else {
            return true
        }
    }
    return false
}