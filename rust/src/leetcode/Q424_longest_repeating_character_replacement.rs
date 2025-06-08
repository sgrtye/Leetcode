/*
 * @lc app=leetcode id=424 lang=rust
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut current_map: HashMap<char, i32> = HashMap::new();
        let mut left: usize = 0;
        let mut max_frequency: i32 = 0;
        let mut result: usize = 0;

        for right in 0..chars.len() {
            *current_map.entry(chars[right]).or_insert(0) += 1;
            if current_map[&chars[right]] > max_frequency {
                max_frequency = current_map[&chars[right]];
            }

            while max_frequency + k < (right - left + 1) as i32 {
                *current_map.get_mut(&chars[left]).unwrap() -= 1;
                left += 1;
            }

            if right - left + 1 > result {
                result = right - left + 1;
            }
        }

        result as i32
    }
}
// @lc code=end
