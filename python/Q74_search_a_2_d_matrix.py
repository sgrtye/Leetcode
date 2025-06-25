#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        left: int = 0
        right: int = rows * cols - 1

        while left <= right:
            mid: int = left + ((right - left) // 2)
            number: int = matrix[mid // cols][mid % cols]

            if number < target:
                left = mid + 1
            elif number > target:
                right = mid - 1
            else:
                return True

        return False


# @lc code=end
