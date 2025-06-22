/*
 * @lc app=leetcode id=152 lang=rust
 *
 * [152] Maximum Product Subarray
 */

// @lc code=start
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut result: i32 = nums[0];
        let mut dp_min: Vec<i32> = vec![nums[0]; nums.len()];
        let mut dp_max: Vec<i32> = vec![nums[0]; nums.len()];

        for i in 1..nums.len() {
            let num: i32 = nums[i];

            if num >= 0 {
                dp_min[i] = num.min(num * dp_min[i - 1]);
                dp_max[i] = num.max(num * dp_max[i - 1]);
            } else {
                dp_min[i] = num.min(num * dp_max[i - 1]);
                dp_max[i] = num.max(num * dp_min[i - 1]);
            }

            result = result.max(dp_max[i]);
        }

        result
    }
}
// @lc code=end
