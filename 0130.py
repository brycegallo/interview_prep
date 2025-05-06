# leetcode 0130 - Surrounded Regions
# Medium - Graphs
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# Time O(n)? Space O(1)?
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def capture(r, c):
            directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            for d_r, d_c in directions:
                capture(r + d_r, c + d_c)
        

        # 1 DFS: capture unsurrounded pieces
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r,c)

        # 2 (Un)Capture (un)surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                # if surrounded, capture
                if board[r][c] == "O":
                    board[r][c] = "X"
                # If unsurrounded, uncapture
                if board[r][c] == "T":
                    board[r][c] = "O"
