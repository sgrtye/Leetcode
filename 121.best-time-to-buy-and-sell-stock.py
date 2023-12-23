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
        l = 0
        r = 1
        current_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = max(current_profit, prices[r] - prices[l])
            else:
                l = r

            r = r + 1

        return current_profit


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
