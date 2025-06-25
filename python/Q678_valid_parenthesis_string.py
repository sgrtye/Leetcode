#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min: int = 0
        left_max: int = 0

        for c in s:
            if c == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1

            if left_max < 0:
                return False

            if left_min < 0:
                left_min = 0

        return left_min == 0


# @lc code=end
