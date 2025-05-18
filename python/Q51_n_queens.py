#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#


# @lc code=start
class Solution:
    def backtrack(self, number: int, stack: list[tuple[int, int]]) -> None:
        if number == self.target:
            result: list[list[str]] = [
                ["." for _ in range(self.target)] for _ in range(self.target)
            ]

            for i, j in stack:
                result[i][j] = "Q"

            self.results.append(["".join(line) for line in result])
            return

        for i in range(self.target):
            if (
                self.col[i]
                or self.pos_diag[number + i]
                or self.neg_diag[number - i + self.target - 1]
            ):
                continue

            self.col[i] = True
            self.pos_diag[number + i] = True
            self.neg_diag[number - i + self.target - 1] = True

            stack.append((number, i))
            self.backtrack(number + 1, stack)
            stack.pop()

            self.col[i] = False
            self.pos_diag[number + i] = False
            self.neg_diag[number - i + self.target - 1] = False

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.col: list[bool] = [False] * n
        self.pos_diag: list[bool] = [False] * (2 * n - 1)
        self.neg_diag: list[bool] = [False] * (2 * n - 1)

        self.target: int = n

        self.results: list[list[str]] = []

        self.backtrack(0, [])

        return self.results


# @lc code=end
