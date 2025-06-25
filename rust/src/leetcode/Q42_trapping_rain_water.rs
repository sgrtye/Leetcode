/*
 * @lc app=leetcode id=42 lang=rust
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left_max: i32 = 0;
        let mut right_max: i32 = 0;

        let mut left: usize = 0;
        let mut right: usize = height.len() - 1;

        let mut result: i32 = 0;

        while left <= right {
            if left_max <= right_max {
                result += (left_max.min(right_max) - height[left]).max(0);
                left_max = left_max.max(height[left]);
                left += 1;
            } else {
                result += (left_max.min(right_max) - height[right]).max(0);
                right_max = right_max.max(height[right]);
                right -= 1;
            }
        }

        result
    }
}
// @lc code=end
