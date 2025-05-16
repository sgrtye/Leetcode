#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # In the order of rows, cols, then boxes ordered from left to right, top to bottom
        check_sets: list[set[str]] = [set() for _ in range(27)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == ".":
                    continue

                box_index: int = i // 3 * 3 + j // 3

                if (
                    char in check_sets[i]
                    or char in check_sets[j + 9]
                    or char in check_sets[box_index + 18]
                ):
                    return False

                check_sets[i].add(char)
                check_sets[j + 9].add(char)
                check_sets[box_index + 18].add(char)

        return True


# @lc code=end
