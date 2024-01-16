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
        low = prices[0]
        high = prices[0]
        profit = 0

        for p in prices:
            if p < low:
                low = p
                high = p
            elif p > high:
                high = p
                profit = max(profit, high - low)
        
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
