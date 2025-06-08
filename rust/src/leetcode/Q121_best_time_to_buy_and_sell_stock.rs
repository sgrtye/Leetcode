/*
 * @lc app=leetcode id=121 lang=rust
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_buy: i32 = prices[0];
        let mut profit: i32 = 0;

        for price in prices {
            if price - min_buy > profit {
                profit = price - min_buy;
            }

            if price < min_buy {
                min_buy = price;
            }
        }

        profit
    }
}
// @lc code=end
