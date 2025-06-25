#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp: list[int] = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[0] if nums[0] > nums[1] else nums[1]

        for i in range(2, len(nums)):
            rob: int = nums[i] + dp[i - 2]
            not_rob: int = dp[i - 1]
            dp[i] = rob if rob > not_rob else not_rob

        return dp[-1]


# @lc code=end
