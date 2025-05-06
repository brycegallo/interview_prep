# leetcode 0269 - Alien Dictionary
# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
#
# You are given a list of strings words from the alien language's dictionary, where the strings in words are
# sorted lexicographically
# by the rules of this new language.
#
# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order
# by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {character: set() for word in words for character in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        visited = {}  # false = visited, true = on the current path
        result = []  # store results in list now, join later

        def dfs(character):
            if character in visited:
                return visited[character]
            visited[character] = True
            for neighbor in adj[character]:
                if dfs(neighbor):
                    return True
            visited[character] = False
            result.append(character)

        for character in adj:
            if dfs(character):
                return ""
        result.reverse()
        return "".join(result)
