/*
 * @lc app=leetcode id=268 lang=rust
 *
 * [268] Missing Number
 */

// @lc code=start
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut result: i32 = nums.len() as i32;

        for (index, number) in nums.into_iter().enumerate() {
            result ^= index as i32 ^ number;
        }

        result
    }
}
// @lc code=end
