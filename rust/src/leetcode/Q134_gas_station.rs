/*
 * @lc app=leetcode id=134 lang=rust
 *
 * [134] Gas Station
 */

// @lc code=start
impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        if gas.iter().sum::<i32>() < cost.iter().sum::<i32>() {
            return -1;
        }

        let mut start: usize = 0;
        let mut current_gas: i32 = 0;

        for i in 0..gas.len() {
            current_gas += gas[i] - cost[i];

            if current_gas < 0 {
                start = i + 1;
                current_gas = 0;
            }
        }

        start as i32
    }
}
// @lc code=end
