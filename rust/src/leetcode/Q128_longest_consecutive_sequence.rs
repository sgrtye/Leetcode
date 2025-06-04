/*
 * @lc app=leetcode id=128 lang=rust
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let num_set: HashSet<i32> = HashSet::from_iter(nums);

        let mut result: i32 = 0;
        for &n in &num_set {
            if num_set.contains(&(n - 1)) {
                continue;
            }

            let mut current_count: i32 = 0;
            let mut current_number: i32 = n;

            while num_set.contains(&current_number) {
                current_count += 1;
                current_number += 1;
            }

            if current_count > result {
                result = current_count;
            }
        }

        result
    }
}
// @lc code=end
