/*
 * @lc app=leetcode id=238 lang=rust
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut product: i32 = 1;
        let mut prefix: Vec<i32> = vec![1; nums.len()];

        for i in 0..nums.len() {
            if i != 0 {
                prefix[i] = product;
            }

            product *= nums[i];
        }

        product = 1;
        let mut suffix: Vec<i32> = vec![1; nums.len()];

        for i in (0..nums.len()).rev() {
            if i != nums.len() - 1 {
                suffix[i] = product;
            }

            product *= nums[i];
        }

        let mut result: Vec<i32> = vec![1; nums.len()];

        for i in 0..nums.len() {
            result[i] = prefix[i] * suffix[i]
        }

        result
    }
}
// @lc code=end
