func twoSum(nums []int, target int) []int {
    // hashmap will work like indices[value] = index
    indices := make(map[int]int)

    // here i will be index and n will be the value at that index in nums
    for i, n := range nums {
	difference := target - n

	// here found will be the other, optional return value from accessing a map
	if j, found := indices[difference]; found {
	    return []int{j, i}
	}
	// if the value of difference isn't found in the hashmap, we add n to the hashmap to serve as a potential difference for other values and target, stored at the index i where it was found
	indices[n] = i
    }
    // this return should never be reached, but may be necessary for runners like leetcode
    return []int{}
}
