#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#


# @lc code=start
class Solution:
    def elapse(self) -> list[tuple[int, int]]:
        new_rotten_list: list[tuple[int, int]] = []

        for i, j in self.rotten:
            for x, y in self.directions:
                if (
                    0 <= i + x < self.ROWS
                    and 0 <= j + y < self.COLS
                    and self.grid[i + x][j + y] == 1
                ):
                    new_rotten_list.append((i + x, j + y))
                    self.grid[i + x][j + y] = 0

        return new_rotten_list

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.ROWS: int = len(grid)
        self.COLS: int = len(grid[0])
        self.grid: list[list[int]] = grid
        self.directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        self.rotten: list[tuple[int, int]] = []
        fresh_oranges: int = 0

        for i in range(self.ROWS):
            for j in range(self.COLS):
                match self.grid[i][j]:
                    case 1:
                        fresh_oranges += 1
                    case 2:
                        self.rotten.append((i, j))
                        self.grid[i][j] = 0

        oranges: int = fresh_oranges + len(self.rotten)
        if oranges == 0:
            return 0

        result: int = -1

        while self.rotten:
            result += 1
            oranges -= len(self.rotten)
            self.rotten = self.elapse()

        return result if oranges == 0 else -1


# @lc code=end
