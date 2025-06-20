/*
 * @lc app=leetcode id=763 lang=rust
 *
 * [763] Partition Labels
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut char_map: HashMap<char, i32> = HashMap::new();
        for (index, c) in s.chars().enumerate() {
            char_map.insert(c, index as i32);
        }

        let mut result: Vec<i32> = Vec::new();
        let mut left: i32 = 0;
        let mut right: i32 = 0;

        for (index, c) in s.chars().enumerate() {
            right = right.max(char_map[&c]);

            if index as i32 == right {
                result.push(right - left + 1);
                left = right + 1;
            }
        }

        result
    }
}
// @lc code=end
