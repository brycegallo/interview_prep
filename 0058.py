# leetcode 0058 - Length of Last Word
# Easy
#
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Time: O(n) Memory: O(1)
class MySolution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if not s[i].isspace():
                length += 1
            elif length:
                break
        return length

class NeetCodeSolution:
    def lengthOfLastWord(self, s: str) -> int:
    # return len(s.split()[-1])  # shortcut, not ideal for interviews
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c