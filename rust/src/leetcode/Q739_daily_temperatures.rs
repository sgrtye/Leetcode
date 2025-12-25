/*
 * @lc app=leetcode id=739 lang=rust
 *
 * [739] Daily Temperatures
 */

// @lc code=start
impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<usize> = vec![];
        let mut result: Vec<i32> = vec![0; temperatures.len()];

        for i in 0..temperatures.len() {
            while let Some(&previous_index) = stack.last() {
                if temperatures[i] > temperatures[previous_index] {
                    stack.pop();
                    result[previous_index] = (i - previous_index) as i32;
                } else {
                    break;
                }
            }

            stack.push(i);
        }

        result
    }
}
// @lc code=end
