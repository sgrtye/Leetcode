#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left: int = 0
        profit: int = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            elif prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]

        return profit


# @lc code=end
