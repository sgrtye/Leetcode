/*
 * @lc app=leetcode id=53 lang=rust
 *
 * [53] Maximum Subarray
 */

// @lc code=start
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut result: i32 = i32::MIN;
        let mut current: i32 = i32::MIN;

        for num in nums {
            if current < 0 {
                current = num;
            } else {
                current += num;
            }

            result = result.max(current);
        }

        result
    }
}
// @lc code=end
