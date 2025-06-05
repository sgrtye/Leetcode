/*
 * @lc app=leetcode id=11 lang=rust
 *
 * [11] Container With Most Water
 */

// @lc code=start
use std::cmp::{max, min};

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut result: i32 = 0;

        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;

        while left < right {
            let current: i32 = (right - left) as i32 * min(height[left], height[right]);

            if current > result {
                result = current
            }

            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }

        result
    }
}
// @lc code=end
