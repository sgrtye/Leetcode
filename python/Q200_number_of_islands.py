#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def dfs(self, row: int, col: int, new_island: bool = False) -> None:
        if (
            row < 0
            or col < 0
            or row >= self.ROWS
            or col >= self.COLS
            or self.grid[row][col] == "0"
        ):
            return

        if new_island:
            self.islands += 1

        self.grid[row][col] = "0"

        for x, y in self.directions:
            self.dfs(row + x, col + y)

    def numIslands(self, grid: list[list[str]]) -> int:
        self.ROWS: int = len(grid)
        self.COLS: int = len(grid[0])
        self.grid: list[list[str]] = grid

        self.islands: int = 0

        self.directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(self.ROWS):
            for y in range(self.COLS):
                self.dfs(x, y, True)

        return self.islands

# @lc code=end
