// Leetcode 0020 - Valid Parentheses
// Easy - Stack
// Given a string s containing just the characters '(', ')', '[', ']', '{', and '}', determine if the input string is valid
// an input string is valid if:
// 1. Open brackets must be closed by the same type of bracket
// 2. Open brackets must be closed in the correct order
// 3. Every close bracket has a corresponding open bracket of the same type
// Stack solution:
// Time Complexity: O(n) Memory: O(n)
bool isValid(char *s) {
    int s_len = strlen(s);
    char stack[s_len] = {};
    int stack_tracker = 0;

    for (int i = 0; i < s_len; i++) {
	char c = s[i];
	
	if (c == '(' || c == '[' || c == '{') {
	    stack[stack_tracker] = c;
	    stack_tracker++;
	}
	else if (stack_tracker != 0) {
	    switch (c) {
	    case ')':
		if (stack[stack_tracker - 1] != '(') { return false } ;
		break;
	    case ']':
		if (stack[stack_tracker - 1] != '[') { return false } ;
		break;
	    case '}':
		if (stack[stack_tracker - 1] != '{') { return false } ;
		break;
	    default:
		printf("Invalid Input");
		break;
	    }
	    stack[stack_tracker - 1] = '\0';
	    stack_tracker--;
	}
	else {
	    return false;
	}
    }
    if (stack_tracker == 0) {
	return true;
    }
    return false;
}

