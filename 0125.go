// Leetcode 0125 - Valid Palindromes
// Easy - Two Pointers
// A phrase is a palindrome if, after convering all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
// Alphanumeric characters include letters and numbers
//
// Given a string s, return true if it is a palindrome, or false otherwise
// Time Complexity O(n) Memory O(1)
func isAlphaNumeric(c rune) bool {
    return unicode.IsLetter(c) || unicode.IsDigit(c)
}

func isPalindrome(s string) bool {
    sRunes := []rune(s)
    i := 0
    j := len(s) - 1

    for i < j {
	for i < j && !isAlphaNumeric(sRunes[i]) {
	    i++
	}
	for i < j && !isAlphaNumeric(sRunes[j]) {
	    j--
	}
	if unicode.ToLower(sRunes[i]) != unicode.ToLower(sRunes[j]) {
	    return false
	}
	i++
	j--
    }
    return false
}
