/*
 * @lc app=leetcode id=139 lang=rust
 *
 * [139] Word Break
 */

// @lc code=start
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let mut dp: Vec<bool> = vec![false; s.len() + 1];
        dp[0] = true;

        for i in 1..=s.len() {
            for word in &word_dict {
                if word.len() <= i && s[i - word.len()..i] == word[..] && dp[i - word.len()] {
                    dp[i] = true;
                    break;
                }
            }
        }

        dp[dp.len() - 1]
    }
}
// @lc code=end
