// Leetcode 0242 - Valid Anagram
// Given two strings s and t, return true if t is an anagram of s, and false otherwise
// s is guaranteed to be at least 1 character, t is not
// Solution with quicksort
// Time Complexity: O(n logn + m logm) Space: O(1) or O(n + m) depending on algorithm
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
	return false
    }

    sRunes, tRunes := []rune(s), []rune(t)

    sort.Slice(sRunes, func(i, j int) bool {
	return sRunes[i], sRunes[j]
    })

    sort.Slice(tRunes, func(i, j int) bool {
	return tRunes[i], tRunes[j]
    })

    for i := range sRunes {
	if sRunes[i] != tRunes[i] {
	    return false
	}
    }
    return true
}

// a hash map solution also exists to be implemented in Go
