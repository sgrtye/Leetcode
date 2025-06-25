#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
class Solution:
    def dfs(self, row: int, col: int, water_map: list[list[bool]]) -> None:
        for i, j in self.directions:
            if (
                0 <= row + i < self.ROWS
                and 0 <= col + j < self.COLS
                and not water_map[row + i][col + j]
                and self.heights[row + i][col + j] >= self.heights[row][col]
            ):
                water_map[row + i][col + j] = True
                self.dfs(row + i, col + j, water_map)

    def check_pacific(self) -> None:
        visiting: set[tuple[int, int]] = set()

        for i in range(self.ROWS):
            self.pacific[i][0] = True
            visiting.add((i, 0))

        for j in range(self.COLS):
            self.pacific[0][j] = True
            visiting.add((0, j))

        for i, j in visiting:
            self.dfs(i, j, self.pacific)

    def check_atlantic(self) -> None:
        visiting: set[tuple[int, int]] = set()

        for i in range(self.ROWS):
            self.atlantic[i][self.COLS - 1] = True
            visiting.add((i, self.COLS - 1))

        for j in range(self.COLS):
            self.atlantic[self.ROWS - 1][j] = True
            visiting.add((self.ROWS - 1, j))

        for i, j in visiting:
            self.dfs(i, j, self.atlantic)

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        self.ROWS: int = len(heights)
        self.COLS: int = len(heights[0])
        self.heights: list[list[int]] = heights

        self.directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        self.pacific: list[list[bool]] = [[False] * self.COLS for _ in range(self.ROWS)]
        self.atlantic: list[list[bool]] = [
            [False] * self.COLS for _ in range(self.ROWS)
        ]

        self.check_pacific()
        self.check_atlantic()

        result: list[list[int]] = []

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.pacific[i][j] and self.atlantic[i][j]:
                    result.append([i, j])

        return result


# @lc code=end
