#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        result: int = 0

        while n != 0:
            n &= n - 1
            result += 1

        return result


# @lc code=end
