# @lcpr-before-debug-begin
from python3problem121 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode id=121 lang=python3
# @lcpr version=30109
#
# [121] Best Time to Buy and Sell Stock
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left: int = 0
        right: int = 0
        profit: int = 0

        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right

            right += 1

        return profit


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
