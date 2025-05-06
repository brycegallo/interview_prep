# leetcode 2390 - Removing Stars From a String
# Medium - Stack
#
# You are given a string s, which contains stars *.
# In one operation, you can:
#     Choose a star in s.
#     Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Note:
#     The input will be generated such that the operation is always possible.
#     It can be shown that the resulting string will always be unique.
# Time: O(n) Memory: O(n)
class MyInitialSolution:
    def removeStars(self, s: str) -> str:
        stack = []

        for character in s:
            stack.append(character)
            if character == "*":
                stack.pop()
                stack.pop()

        return "".join(stack)


class NeetcodeSolution:
    def removeStars(self, s: str) -> str:
        stack = []

        for character in s:
            if character == "*":
                stack and stack.pop()
            else:
                stack.append(character)

        return "".join(stack)
