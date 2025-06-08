/*
 * @lc app=leetcode id=3 lang=rust
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut current_set: HashSet<char> = HashSet::new();
        let mut left: usize = 0;
        let mut result: usize = 0;

        for right in 0..chars.len() {
            while current_set.contains(&chars[right]) {
                current_set.remove(&chars[left]);
                left += 1;
            }

            current_set.insert(chars[right]);

            if right - left + 1 > result {
                result = right - left + 1;
            }
        }

        result as i32
    }
}
// @lc code=end
