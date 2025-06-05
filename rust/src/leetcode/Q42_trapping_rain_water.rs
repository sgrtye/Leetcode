/*
 * @lc app=leetcode id=42 lang=rust
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
use std::cmp::{max, min};

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left_max: i32 = 0;
        let mut right_max: i32 = 0;

        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;

        let mut result: i32 = 0;

        while left <= right {
            if left_max <= right_max {
                result += max(min(left_max, right_max) - height[left], 0);
                left_max = max(left_max, height[left]);
                left += 1;
            } else {
                result += max(min(left_max, right_max) - height[right], 0);
                right_max = max(right_max, height[right]);
                right -= 1;
            }
        }

        result
    }
}
// @lc code=end
