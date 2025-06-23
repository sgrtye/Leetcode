/*
 * @lc app=leetcode id=1143 lang=rust
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let text1: Vec<char> = text1.chars().collect();
        let text2: Vec<char> = text2.chars().collect();

        let mut dp: Vec<Vec<i32>> = vec![vec![0; text2.len() + 1]; text1.len() + 1];

        for i in 1..=text1.len() {
            for j in 1..=text2.len() {
                if text1[i - 1] == text2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);
                }
            }
        }

        dp[dp.len() - 1][dp[0].len() - 1]
    }
}
// @lc code=end
