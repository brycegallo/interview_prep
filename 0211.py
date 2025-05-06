# leetcode 0211 - Design Add and Search Words Data Structure
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#     WordDictionary() Initializes the object.
#     void addWord(word) Adds word to the data structure, it can be matched later.
#     bool search(word) Returns true if there is any string in the data structure that matches word
#     or false otherwise. word may contain dots '.' where dots can be matched with any letter.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                character = word[i]
                if character == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if character not in cur.children:
                        return False
                    cur = cur.children[character]
            return cur.word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
