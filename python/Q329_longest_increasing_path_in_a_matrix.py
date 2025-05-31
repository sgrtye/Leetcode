#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def dfs(self, row: int, col: int) -> int:
        if self.dp[row][col] != -1:
            return self.dp[row][col]

        result: int = 0

        for x, y in self.directions:
            new_row: int = row + x
            new_col: int = col + y
            if (
                0 <= new_row < self.ROWS
                and 0 <= new_col < self.COLS
                and self.matrix[row][col] < self.matrix[new_row][new_col]
            ):
                if (new_max := self.dfs(new_row, new_col)) > result:
                    result = new_max

        self.dp[row][col] = result + 1
        return result + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.ROWS: int = len(matrix)
        self.COLS: int = len(matrix[0])
        self.matrix: list[list[int]] = matrix

        self.dp: list[list[int]] = [[-1] * self.COLS for _ in range(self.ROWS)]
        self.directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        result: int = 0

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if (new_max := self.dfs(i, j)) > result:
                    result = new_max

        return result


# @lc code=end
