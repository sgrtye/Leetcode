/*
 * @lc app=leetcode id=55 lang=rust
 *
 * [55] Jump Game
 */

// @lc code=start
impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut jump: usize = nums.len() - 1;

        for i in (0..nums.len() - 1).rev() {
            if nums[i] as usize + i >= jump {
                jump = i
            }
        }

        jump == 0
    }
}
// @lc code=end
