// Leetcode 0344 - Reverse String
// Easy - Two Pointers
// Write a function that reverse a string. The input string is given as an array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory
// Two-Pointer Solution
// Time Complexity: O(n) Memory: O(1)
void reverseString(char* s, int sSize) {
    int left = 0;
    int right = sSize - 1;
    while (left < right) {
	char placeholder = s[left];
	s[left] = s[right];
	s[right] = placeholder;
	left++;
	right--;
    }
}
