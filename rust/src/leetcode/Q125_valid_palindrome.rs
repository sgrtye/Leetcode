/*
 * @lc app=leetcode id=125 lang=rust
 *
 * [125] Valid Palindrome
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let cleaned: String = s
            .to_lowercase()
            .chars()
            .filter(|c| c.is_alphanumeric())
            .collect();

        if cleaned.is_empty() {
            return true;
        }

        let chars: Vec<char> = cleaned.chars().collect();
        let mut left: usize = 0;
        let mut right: usize = cleaned.len().saturating_sub(1);

        while left < right {
            if chars[left] != chars[right] {
                return false;
            }

            left += 1;
            right -= 1;
        }

        true
    }
}
// @lc code=end
