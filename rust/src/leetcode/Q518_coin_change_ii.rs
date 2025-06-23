/*
 * @lc app=leetcode id=518 lang=rust
 *
 * [518] Coin Change II
 */

// @lc code=start
impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let mut dp: Vec<Vec<i32>> = vec![vec![0; amount as usize + 1]; coins.len() + 1];

        for i in 0..=coins.len() {
            dp[i][0] = 1;
        }

        for i in 1..=coins.len() {
            for j in 1..=amount as usize {
                let coin: i32 = coins[i - 1];

                if j < coin as usize {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coin as usize];
                }
            }
        }

        dp[coins.len()][amount as usize]
    }
}
// @lc code=end
