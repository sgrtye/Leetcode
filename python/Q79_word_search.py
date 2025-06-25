#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def search(self, row: int, col: int, index: int) -> bool:
        if index == self.target:
            return True

        # out of bounds, visited cell, wrong letter
        if (
            row < 0
            or col < 0
            or row >= self.ROWS
            or col >= self.COLS
            or self.visiting[row][col]
            or self.board[row][col] != self.word[index]
        ):
            return False

        self.visiting[row][col] = True
        result: bool = any(
            self.search(row + d1, col + d2, index + 1) for d1, d2 in self.directions
        )
        self.visiting[row][col] = False

        return result

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.ROWS: int = len(board)
        self.COLS: int = len(board[0])

        self.board: list[list[str]] = board
        self.word: str = word
        self.target: int = len(self.word)

        self.directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visiting: list[list[bool]] = [
            [False for _ in range(self.COLS)] for _ in range(self.ROWS)
        ]

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.search(i, j, 0):
                    return True

        return False


# @lc code=end
