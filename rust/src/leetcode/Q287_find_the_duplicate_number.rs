/*
 * @lc app=leetcode id=287 lang=rust
 *
 * [287] Find the Duplicate Number
 */

// @lc code=start
impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut slow1: usize = 0;
        let mut fast: usize = 0;

        loop {
            slow1 = nums[slow1] as usize;
            fast = nums[nums[fast] as usize] as usize;

            if slow1 == fast {
                break;
            }
        }

        let mut slow2: usize = 0;

        loop {
            slow1 = nums[slow1] as usize;
            slow2 = nums[slow2] as usize;

            if slow1 == slow2 {
                return slow1 as i32;
            }
        }
    }
}
// @lc code=end
