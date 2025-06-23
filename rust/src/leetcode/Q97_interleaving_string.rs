/*
 * @lc app=leetcode id=97 lang=rust
 *
 * [97] Interleaving String
 */

// @lc code=start
impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let s1: Vec<char> = s1.chars().collect();
        let s2: Vec<char> = s2.chars().collect();
        let s3: Vec<char> = s3.chars().collect();

        if s1.len() + s2.len() != s3.len() {
            return false;
        }

        let mut dp: Vec<Vec<bool>> = vec![vec![false; s2.len() + 1]; s1.len() + 1];
        dp[0][0] = true;

        for i in 0..=s1.len() {
            for j in 0..=s2.len() {
                if (i != 0 && dp[i - 1][j] && s1[i - 1] == s3[i + j - 1])
                    || (j != 0 && dp[i][j - 1] && s2[j - 1] == s3[i + j - 1])
                {
                    dp[i][j] = true;
                }
            }
        }

        dp[s1.len()][s2.len()]
    }
}
// @lc code=end
