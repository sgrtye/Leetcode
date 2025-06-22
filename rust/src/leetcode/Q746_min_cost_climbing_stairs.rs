/*
 * @lc app=leetcode id=746 lang=rust
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut steps: Vec<i32> = vec![0; cost.len() + 1];

        for i in 2..=cost.len() {
            steps[i] = (steps[i - 1] + cost[i - 1]).min(steps[i - 2] + cost[i - 2]);
        }

        steps[steps.len() - 1]
    }
}
// @lc code=end
