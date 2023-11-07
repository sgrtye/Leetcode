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
        sub_boards = [[] for _ in range(27)]
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    sub_boards[i].append(element)
                    sub_boards[j + 9].append(element)
                    sub_boards[i//3*3 + j//3 + 18].append(element)
        
        for sub in sub_boards:
            if len(sub) != len(set(sub)):
                return False
        
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

