# leetcode 0079 - Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()  # add current values from path to avoid revisiting

        # nest depth first search
        def dfs(row, col, i):  # i is the current character in the target word string
            if i == len(word):  # if we reach the end of the word, we know we've found it
                return True
            # if row or column is less than zero, we've left the board
            # if row/column is greater than the number of rows/columns, we've also left the board
            # if the letter we're at is not equal to the character we're at on the board
            # if the (row, col) position we're at is in the path set, we've already visited it
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                word[i] != board[row][col] or
                (row, col) in path):
                return False

            # if neither condition satisfies, we've found a character we're looking for
            path.add((row, col))
            res = (dfs(row + 1, col, i + 1) or
                   dfs(row - 1, col, i + 1) or
                   dfs(row, col + 1, i + 1) or
                   dfs(row, col - 1, i + 1))
            path.remove((row, col))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0): return True
        return False



