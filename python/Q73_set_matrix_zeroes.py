#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        rows: set[int] = set()
        cols: set[int] = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(ROWS):
            if i in rows:
                for j in range(COLS):
                    matrix[i][j] = 0

        for j in range(COLS):
            if j in cols:
                for i in range(ROWS):
                    matrix[i][j] = 0


# @lc code=end
