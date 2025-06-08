/*
 * @lc app=leetcode id=567 lang=rust
 *
 * [567] Permutation in String
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let s1_vec: Vec<char> = s1.chars().collect();
        let mut s1_map: HashMap<char, i32> = HashMap::new();
        for c in s1_vec {
            *s1_map.entry(c).or_insert(0) += 1;
        }

        let s2_vec: Vec<char> = s2.chars().collect();
        let mut s2_map: HashMap<char, i32> = HashMap::new();

        let mut left: usize = 0;
        let mut remained: usize = s1_map.len();

        for right in 0..s2_vec.len() {
            let right_char: char = s2_vec[right];

            if !s1_map.contains_key(&right_char) {
                remained = s1_map.len();
                s2_map.clear();
                left = right + 1;
                continue;
            }

            *s2_map.entry(right_char).or_insert(0) += 1;

            if s1_map.get(&right_char) == s2_map.get(&right_char) {
                remained -= 1;
                if remained == 0 {
                    return true;
                }
            } else {
                while s1_map.get(&right_char) < s2_map.get(&right_char) {
                    let left_char: char = s2_vec[left];

                    if s1_map.get(&left_char) == s2_map.get(&left_char) {
                        remained += 1;
                    }

                    *s2_map.get_mut(&left_char).unwrap() -= 1;
                    left += 1;
                }
            }
        }

        false
    }
}
// @lc code=end
