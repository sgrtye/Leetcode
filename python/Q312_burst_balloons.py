#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#


# @lc code=start
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n: int = len(nums)
        new_nums: list[int] = [1] + nums + [1]

        dp: list[list[int]] = [[0] * (n + 2) for _ in range(n + 2)]

        for left in range(n, 0, -1):
            for right in range(left, n + 1):
                for i in range(left, right + 1):
                    coins: int = new_nums[left - 1] * new_nums[i] * new_nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n]


# @lc code=end
