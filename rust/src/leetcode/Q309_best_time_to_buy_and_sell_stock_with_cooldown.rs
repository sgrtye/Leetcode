/*
 * @lc app=leetcode id=309 lang=rust
 *
 * [309] Best Time to Buy and Sell Stock with Cooldown
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut bought: Vec<i32> = vec![-prices[0]; prices.len()];
        let mut sold: Vec<i32> = vec![0; prices.len()];
        let mut chilled: Vec<i32> = vec![0; prices.len()];

        for i in 1..prices.len() {
            bought[i] = bought[i - 1].max(chilled[i - 1] - prices[i]);
            sold[i] = bought[i - 1] + prices[i];
            chilled[i] = chilled[i - 1].max(sold[i - 1]);
        }

        sold[sold.len() - 1].max(chilled[chilled.len() - 1])
    }
}
// @lc code=end
