/*
 * @lc app=leetcode id=66 lang=rust
 *
 * [66] Plus One
 */

// @lc code=start
impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = digits;

        for i in (0..result.len()).rev() {
            if result[i] < 9 {
                result[i] += 1;
                return result;
            } else {
                result[i] = 0;
            }
        }

        let mut extended_result: Vec<i32> = vec![1];
        extended_result.extend(result);
        extended_result
    }
}
// @lc code=end
