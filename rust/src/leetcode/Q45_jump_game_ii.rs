/*
 * @lc app=leetcode id=45 lang=rust
 *
 * [45] Jump Game II
 */

// @lc code=start
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        let mut left: usize = 0;
        let mut right: usize = 0;

        while right < nums.len() - 1 {
            let mut right_most: usize = left;

            for i in left..=right {
                right_most = right_most.max(nums[i] as usize + i);
            }

            result += 1;
            left = right + 1;
            right = right_most;
        }

        result
    }
}
// @lc code=end
