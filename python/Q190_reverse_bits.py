#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result: int = 0

        for i in range(32):
            result = (n >> i) & 1 | (result << 1)

        return result


# @lc code=end
