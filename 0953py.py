# leetcode 0953. Verifying an Alien Dictionary
# Easy - Graphs
#
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographically in this alien language.
# Time: O(m) Memory: O(1) where n is the total number of characters in all words
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIndex = {character: i for i, character in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if orderIndex[word2[j]] < orderIndex[word1[j]]:
                        return False
                    break

        return True
