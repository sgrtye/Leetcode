/*
 * @lc app=leetcode id=72 lang=rust
 *
 * [72] Edit Distance
 */

// @lc code=start
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let word1: Vec<char> = word1.chars().collect();
        let word2: Vec<char> = word2.chars().collect();

        let mut dp: Vec<Vec<i32>> = vec![vec![0; word2.len() + 1]; word1.len() + 1];

        for i in 0..=word1.len() {
            dp[i][0] = i as i32;
        }
        for j in 0..=word2.len() {
            dp[0][j] = j as i32;
        }

        for i in 1..=word1.len() {
            for j in 1..=word2.len() {
                if word1[i - 1] == word2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i - 1][j - 1].min(dp[i - 1][j].min(dp[i][j - 1])) + 1;
                }
            }
        }

        dp[word1.len()][word2.len()]
    }
}
// @lc code=end
