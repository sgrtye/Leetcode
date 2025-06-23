/*
 * @lc app=leetcode id=10 lang=rust
 *
 * [10] Regular Expression Matching
 */

// @lc code=start
impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let p: Vec<char> = p.chars().collect();

        let mut dp: Vec<Vec<bool>> = vec![vec![false; p.len() + 1]; s.len() + 1];
        dp[0][0] = true;

        for j in 1..=p.len() {
            if p[j - 1] == '*' {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for i in 1..=s.len() {
            for j in 1..=p.len() {
                if s[i - 1] == p[j - 1] || p[j - 1] == '.' {
                    dp[i][j] = dp[i - 1][j - 1];
                }

                if p[j - 1] == '*' {
                    dp[i][j] = dp[i][j - 2];

                    if p[j - 2] == '.' || s[i - 1] == p[j - 2] {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                }
            }
        }

        dp[s.len()][p.len()]
    }
}
// @lc code=end
