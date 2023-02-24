# leetcode 0076 - Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
# every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if input string of necessary characters is empty, return it
        if not t: return t

        # initialize empty maps for count of all necessary characters and count of characters in window
        countT, window = {}, {}
        # add every character in the necessary characters string into the count
        for character in t:
            countT[character] = 1 + countT.get(character, 0)

        # initialize count of necessary letters that we have to 0
        # initialize count of necessary letters total to length of necessary characters string
        have, need = 0, len(countT)
        # initialize result to location which is not in the hash map, length to infinity (because we want to minimize it)
        result, result_length = [-1, -1], float("infinity")
        left = 0

        # iterate through every character in the input string, using each as a right pointer
        for right in range(len(s)):
            character = s[right]
            window[character] = 1 + window.get(character, 0)

            if character in countT and window[character] == countT[character]:
                have += 1

            while have == need:
                if (right - left + 1) < result_length:
                    result = [left, right]
                    result_length = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left: right + 1] if result_length != float("infinity") else ""
