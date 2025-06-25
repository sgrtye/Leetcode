#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp1: list[int] = [0] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2: list[int] = [0] * (len(nums) - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            rob: int = nums[i] + dp1[i - 2]
            not_rob: int = dp1[i - 1]
            dp1[i] = rob if rob > not_rob else not_rob

            rob: int = nums[i + 1] + dp2[i - 2]
            not_rob: int = dp2[i - 1]
            dp2[i] = rob if rob > not_rob else not_rob

        return max(dp1[-1], dp2[-1])


# @lc code=end
