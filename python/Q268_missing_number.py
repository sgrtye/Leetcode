#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result: int = len(nums)

        for i, v in enumerate(nums):
            result ^= i ^ v

        return result


# @lc code=end
