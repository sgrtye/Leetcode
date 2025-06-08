/*
 * @lc app=leetcode id=76 lang=rust
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        let t_vec: Vec<char> = t.chars().collect();
        let mut t_map: HashMap<char, i32> = HashMap::new();
        for c in t_vec {
            *t_map.entry(c).or_insert(0) += 1;
        }

        let s_vec: Vec<char> = s.chars().collect();
        let mut s_map: HashMap<char, i32> = HashMap::new();

        let mut left: usize = 0;
        let mut remained: usize = t_map.len();

        let mut result_start: usize = 0;
        let mut result_length: usize = s.len() + 1;

        for right in 0..s_vec.len() {
            let right_char: char = s_vec[right];
            *s_map.entry(right_char).or_insert(0) += 1;

            if s_map.get(&right_char) == t_map.get(&right_char) {
                remained -= 1;

                while remained == 0 {
                    if right - left + 1 < result_length {
                        result_start = left;
                        result_length = right - left + 1;
                    }

                    let left_char = s_vec[left];

                    if s_map.get(&left_char) == t_map.get(&left_char) {
                        remained += 1;
                    }

                    *s_map.get_mut(&left_char).unwrap() -= 1;
                    left += 1;
                }
            }
        }

        if result_length == s.len() + 1 {
            String::new()
        } else {
            s_vec[result_start..result_start + result_length]
                .iter()
                .collect()
        }
    }
}
// @lc code=end
