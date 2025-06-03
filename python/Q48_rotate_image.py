#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    def rotate_layer(self, matrix: list[list[int]], left: int, right: int) -> None:
        for i in range(right - left):
            value: int = matrix[left][left + i]

            matrix[left][left + i] = matrix[right - i][left]
            matrix[right - i][left] = matrix[right][right - i]
            matrix[right][right - i] = matrix[left + i][right]
            matrix[left + i][right] = value

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left: int = 0
        right: int = len(matrix) - 1

        while left <= right:
            self.rotate_layer(matrix, left, right)
            left += 1
            right -= 1


# @lc code=end
