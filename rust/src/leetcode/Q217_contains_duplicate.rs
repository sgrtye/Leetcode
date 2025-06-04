/*
 * @lc app=leetcode id=217 lang=rust
 *
 * [217] Contains Duplicate
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen: HashSet<i32> = HashSet::new();

        for n in nums {
            if !seen.insert(n) {
                return true;
            }
        }

        false
    }
}
// @lc code=end
