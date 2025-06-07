/*
 * @lc app=leetcode id=704 lang=rust
 *
 * [704] Binary Search
 */

// @lc code=start
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = nums.len() as i32 - 1;

        while left <= right {
            let mid: i32 = left + ((right - left) / 2);

            if nums[mid as usize] == target {
                return mid;
            }

            if nums[mid as usize] < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        -1
    }
}
// @lc code=end
