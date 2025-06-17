/*
 * @lc app=leetcode id=131 lang=rust
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start
impl Solution {
    fn is_palindrome(word: &Vec<char>, mut left: usize, mut right: usize) -> bool {
        while left < right {
            if word[left] == word[right] {
                left += 1;
                right -= 1;
            } else {
                return false;
            }
        }

        true
    }

    fn backtrack(
        s: &Vec<char>,
        current: &mut Vec<String>,
        result: &mut Vec<Vec<String>>,
        index: usize,
    ) {
        if index == s.len() {
            result.push(current.clone());
            return;
        }

        for i in index..s.len() {
            if Self::is_palindrome(s, index, i) {
                let palindrome: String = s[index..i + 1].iter().collect();

                current.push(palindrome);

                Self::backtrack(s, current, result, i + 1);

                current.pop();
            }
        }
    }

    pub fn partition(s: String) -> Vec<Vec<String>> {
        let s: Vec<char> = s.chars().collect();

        let mut result: Vec<Vec<String>> = Vec::new();
        let mut current: Vec<String> = Vec::new();

        Self::backtrack(&s, &mut current, &mut result, 0);

        result
    }
}
// @lc code=end
