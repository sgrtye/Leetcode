/*
 * @lc app=leetcode id=647 lang=rust
 *
 * [647] Palindromic Substrings
 */

// @lc code=start
impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        let mut result: i32 = 0;
        let word: Vec<char> = s.chars().collect();
        let mut dp: Vec<Vec<bool>> = vec![vec![false; word.len()]; word.len()];

        for i in (0..word.len()).rev() {
            for j in i..word.len() {
                if word[i] == word[j] && (j - i <= 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    result += 1;
                }
            }
        }

        result
    }
}
// @lc code=end
