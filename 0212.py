# leetcode 0212 - Word Search II
# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
# Time()
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        current = self
        self.refs += 1
        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
            current.refs += 1
        current.isWord = True

    def removeWord(self, word):
        current = self
        self.refs -= 1
        for character in word:
            if character in current.children:
                current = current.children[character]
                current.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, columns = len(board), len(board[0])
        result, visited = set(), set()

        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(in_row, in_column, node, word):
            if (in_row not in range(rows) or in_column not in range(columns) or
                    board[in_row][in_column] not in node.children or
                    node.children[board[in_row][in_column]].refs < 1 or
                    (in_row, in_column) in visited):
                return None

            visited.add((in_row, in_column))
            node = node.children[board[in_row][in_column]]
            word += board[in_row][in_column]
            if node.isWord:
                node.isWord = False
                result.add(word)
                root.removeWord(word)

            for d_row, d_column in directions:
                dfs(in_row + d_row, in_column + d_column, node, word)
            visited.remove((in_row, in_column))

        for row in range(rows):
            for column in range(columns):
                dfs(row, column, root, "")

        return list(result)
