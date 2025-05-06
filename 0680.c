// Leetcode 0680 - Valid Palindrome II
// Easy - Two Pointers
// Given a string s, return true if s can be a palindrome after deleting at most one character from it
// Two-Pointer Solution - i believe this is the most optimal use of a helper function
// Time Complexity: O(n) Memory: O(1)
bool isPalindrome(char* s, int left, int right) {
    int i = left;
    int j = right;
    while (i < j) {
        while (i < j && !isalnum(s[i])) {
            i++;
        }
        while ( i < j && !isalnum(s[j])) {
            j--;
        }
        if (tolower(s[i]) != tolower(s[j])) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

bool validPalindrome(char* s) {
    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        while (left < right && !isalnum(s[left])) {
            left++;
        }
        while (left < right && !isalnum(s[right])) {
            right--;
        }
        if (tolower(s[left]) != tolower(s[right])) {
            return (isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1));
        }
        left++;
        right--;
    }
    return true;
}
