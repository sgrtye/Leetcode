#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result: int = 0

        for n in nums:
            result ^= n

        return result


# @lc code=end
