/*
 * @lc app=leetcode id=242 lang=rust
 *
 * [242] Valid Anagram
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut char_count: HashMap<char, i32> = HashMap::new();

        for c in s.chars() {
            *char_count.entry(c).or_insert(0) += 1;
        }

        for c in t.chars() {
            *char_count.entry(c).or_insert(0) -= 1;
        }

        char_count.into_values().all(|count| count == 0)
    }
}
// @lc code=end
