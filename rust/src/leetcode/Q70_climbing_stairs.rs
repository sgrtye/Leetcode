/*
 * @lc app=leetcode id=70 lang=rust
 *
 * [70] Climbing Stairs
 */

// @lc code=start
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut steps: Vec<i32> = vec![1; n as usize + 1];

        for i in 2..=n as usize {
            steps[i] = steps[i - 1] + steps[i - 2];
        }

        steps[steps.len() - 1]
    }
}
// @lc code=end
