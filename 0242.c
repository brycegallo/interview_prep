// Leetcode 0242: Valid Anagram
// Given two strings s and t, return true if t is an anagram of s, and false otherwise
// s is guaranteed to be at least 1 character, t is not
// Sort with qsort()
// Time Complexity: O(n logn) Space Complexity: O(1)
int compare (const void* a, const void* b) {
    char* char_a = a;
    char* char_b = b;
    return *char_a - *char_b;
}

bool isAnagram(char* s, char* t) {
    if (strlen(s) != strlen(t)) {
	return false;
    }
    qsort(s, strlen(s), sizeof(s[0]), compare);
    qsort(t, strlen(t), sizeof(t[0]), compare);
    for (int i = 0; i < strlen(s); i++) {
	of (s[i] != t[i]) {
	    return false;
	}
    }
    return true;
}
