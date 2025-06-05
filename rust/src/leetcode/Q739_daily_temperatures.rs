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
            while !stack.is_empty() && temperatures[i] > temperatures[*stack.last().unwrap()] {
                let index: usize = stack.pop().unwrap();
                result[index] = (i - index) as i32;
            }

            stack.push(i);
        }

        result
    }
}
// @lc code=end
