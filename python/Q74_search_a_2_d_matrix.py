#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        l: int = 0
        r: int = rows * cols - 1

        while l <= r:
            m: int = l + ((r - l) // 2)
            number: int = matrix[m // cols][m % cols]

            if number < target:
                l = m + 1
            elif number > target:
                r = m - 1
            else:
                return True

        return False


# @lc code=end
