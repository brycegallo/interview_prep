# leetcode 0417 - Pacific Atlantic Water Flow
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells.
# You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level
# of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly
# north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
# Water can flow from any cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that
# rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        rows, columns = len(heights),len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # up, down, left, right

        def dfs(visited, in_row, in_column):
            visited.add((in_row,in_column))
            for d_row, d_column in directions:
                new_row, new_column = in_row + d_row, in_column + d_column
                if (new_row in range(rows) and new_column in range(columns) and
                    (new_row, new_column) not in visited and
                    heights[new_row][new_column]>=heights[in_row][in_column]):
                    dfs(visited, new_row, new_column)

        # iterate through rows starting at top
        for row in range(rows):
            dfs(pacific, row, 0)
            dfs(atlantic, row, columns-1)
        # iterate through columns starting from left
        for column in range(columns):
            dfs(pacific, 0, column)
            dfs(atlantic, rows-1, column)

        return list(pacific & atlantic)
