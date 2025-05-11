#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l: int = 0
        profit: int = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            elif prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]

        return profit


# @lc code=end
