#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc code=start
class Solution:
    def dfs(self, row: int, col: int) -> None:
        if (
            row < 0
            or row >= self.ROWS
            or col < 0
            or col >= self.COLS
            or self.board[row][col] != "O"
        ):
            return

        self.board[row][col] = "P"

        for i, j in self.directions:
            self.dfs(row + i, col + j)

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.ROWS: int = len(board)
        self.COLS: int = len(board[0])

        self.board: list[list[str]] = board
        self.directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(self.ROWS):
            self.dfs(i, 0)
            self.dfs(i, self.COLS - 1)

        for j in range(self.COLS):
            self.dfs(0, j)
            self.dfs(self.ROWS - 1, j)

        for i in range(self.ROWS):
            for j in range(self.COLS):
                match board[i][j]:
                    case "O":
                        board[i][j] = "X"
                    case "P":
                        board[i][j] = "O"


# @lc code=end
