#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


# @lc code=start
class Solution:
    def dfs(self, row: int, col: int) -> int:
        if (
            row < 0
            or col < 0
            or row >= self.ROWS
            or col >= self.COLS
            or self.grid[row][col] == 0
        ):
            return 0

        area: int = 1

        self.grid[row][col] = 0
        for x, y in self.directions:
            area += self.dfs(row + x, col + y)

        return area

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.ROWS: int = len(grid)
        self.COLS: int = len(grid[0])
        self.grid: list[list[int]] = grid

        self.max_area: int = 0

        self.directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(self.ROWS):
            for y in range(self.COLS):
                if (new_area := self.dfs(x, y)) > self.max_area:
                    self.max_area = new_area

        return self.max_area


# @lc code=end
