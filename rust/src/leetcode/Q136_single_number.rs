/*
 * @lc app=leetcode id=136 lang=rust
 *
 * [136] Single Number
 */

// @lc code=start
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;

        for n in nums {
            result ^= n;
        }

        result
    }
}
// @lc code=end
