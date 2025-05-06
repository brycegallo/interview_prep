// Leetcode 0125: Valid Palindrome
// Easy - Two Pointers
// A phrase is a palindrome if, after convering all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
// Alphanumeric characters include letters and numbers
//
// Given a string s, return true if it is a palindrome, or false otherwise
// Time Complexity O(n) Memory O(1)

bool isPalindrome(char* s) {
    int i = 0;
    int j = strlen(s) - 1;

    while (i < j) {
	while (i < j && !isalnum(s[i])) {
	    i++;
	}
	while (i < j && !isalnum(s[j])) {
	    j--;
	}
	if (tolower(s[i]) != tolower(s[j])) {
	    return false;
	}
	i++;
	j++;
    }
    return true;
}
