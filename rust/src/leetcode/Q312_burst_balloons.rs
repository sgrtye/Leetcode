/*
 * @lc app=leetcode id=312 lang=rust
 *
 * [312] Burst Balloons
 */

// @lc code=start
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let n: usize = nums.len();

        let mut new_nums: Vec<i32> = vec![1];
        new_nums.extend(nums);
        new_nums.push(1);

        let mut dp: Vec<Vec<i32>> = vec![vec![0; n + 2]; n + 2];

        for l in (1..=n).rev() {
            for r in l..=n {
                for i in l..=r {
                    let coins: i32 = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                        + dp[l][i - 1]
                        + dp[i + 1][r];

                    dp[l][r] = dp[l][r].max(coins);
                }
            }
        }

        dp[1][n]
    }
}
// @lc code=end
