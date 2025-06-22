/*
 * @lc app=leetcode id=213 lang=rust
 *
 * [213] House Robber II
 */

// @lc code=start
impl Solution {
    fn rob_linear(nums: &[i32]) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }

        let mut profit: Vec<i32> = vec![0; nums.len()];
        profit[0] = nums[0];
        profit[1] = nums[0].max(nums[1]);

        for i in 2..nums.len() {
            profit[i] = (profit[i - 1]).max(profit[i - 2] + nums[i]);
        }

        profit[profit.len() - 1]
    }

    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }

        Self::rob_linear(&nums[0..nums.len() - 1]).max(Self::rob_linear(&nums[1..]))
    }
}
// @lc code=end
