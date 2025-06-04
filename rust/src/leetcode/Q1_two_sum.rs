/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result: HashMap<i32, i32> = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            if let Some(&idx) = result.get(&num) {
                return vec![idx, i as i32];
            }

            result.insert(target - num, i as i32);
        }

        vec![]
    }
}
// @lc code=end
