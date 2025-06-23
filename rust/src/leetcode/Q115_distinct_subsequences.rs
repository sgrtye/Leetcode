/*
 * @lc app=leetcode id=115 lang=rust
 *
 * [115] Distinct Subsequences
 */

// @lc code=start
impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();

        let mut dp: Vec<Vec<i32>> = vec![vec![0; t.len() + 1]; s.len() + 1];
        for i in 0..=s.len() {
            dp[i][0] = 1;
        }

        for i in 1..=s.len() {
            for j in 1..=t.len() {
                if s[i - 1] == t[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        dp[s.len()][t.len()]
    }
}
// @lc code=end
