/*
 * @lc app=leetcode id=5 lang=rust
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let mut start: usize = 0;
        let mut length: usize = 0;

        let word: Vec<char> = s.chars().collect();
        let mut dp: Vec<Vec<bool>> = vec![vec![false; word.len()]; word.len()];

        for i in (0..word.len()).rev() {
            for j in i..word.len() {
                if word[i] == word[j] && (j - i <= 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;

                    if j - i + 1 > length {
                        start = i;
                        length = j - i + 1;
                    }
                }
            }
        }

        word[start..start + length].iter().collect()
    }
}
// @lc code=end
