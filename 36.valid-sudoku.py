# @lcpr-before-debug-begin
from python3problem36 import *
from typing import *
import itertools

# @lcpr-before-debug-end

#
# @lc app=leetcode id=36 lang=python3
# @lcpr version=30105
#
# [36] Valid Sudoku
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_set: list[set[int]] = [set() for _ in range(27)]

        for i, j in itertools.product(range(9), range(9)):
            element: str = board[i][j]

            if element == ".":
                continue

            if (
                element in check_set[i]
                or element in check_set[j + 9]
                or element in check_set[i // 3 * 3 + j // 3 + 18]
            ):
                return False
            else:
                check_set[i].add(element)
                check_set[j + 9].add(element)
                check_set[i // 3 * 3 + j // 3 + 18].add(element)

        return True


# @lc code=end


#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
