#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy: list[int] = [-prices[0] for _ in range(len(prices))]
        sell: list[int] = [0 for _ in range(len(prices))]
        cooldown: list[int] = [0 for _ in range(len(prices))]

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])
            sell[i] = buy[i - 1] + prices[i]
            cooldown[i] = max(sell[i - 1], cooldown[i - 1])

        return max(sell[-1], cooldown[-1])


# @lc code=end
