// Leetcode 0125: Valid Palindrome
// Given a string s, return true if it is a palindrome, or false otherwise

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
