#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        positive: bool = x > 0
        x = abs(x)

        result: int = 0

        while x:
            digit: int = x % 10

            if result > (0x7FFFFFFF // 10) or (
                result == (0x7FFFFFFF // 10) and digit > 7
            ):
                return 0
            if result < (-0x80000000 // 10) or (
                result == (-0x80000000 // 10) and digit > 8
            ):
                return 0

            result = (result << 3) + (result << 1) + digit

            x //= 10

        return result if positive else -result


# @lc code=end
