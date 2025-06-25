#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp: list[list[int]] = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                coin: int = coins[i - 1]

                if j < coin:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coin]

        return dp[-1][-1]


# @lc code=end
