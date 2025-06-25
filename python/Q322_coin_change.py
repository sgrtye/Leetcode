#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: list[int] = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0 and (new_value := dp[i - c] + 1) < dp[i]:
                    dp[i] = new_value

        return dp[-1] if dp[-1] <= amount else -1


# @lc code=end
