/*
 * @lc app=leetcode id=153 lang=rust
 *
 * [153] Find Minimum in Rotated Sorted Array
 */

// @lc code=start
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = nums.len() as i32 - 1;

        while left <= right {
            let mid: i32 = left + ((right - left) / 2);

            let left_sorted: bool = nums[left as usize] <= nums[mid as usize];
            let right_sorted: bool = nums[mid as usize] <= nums[right as usize];

            match (left_sorted, right_sorted) {
                (true, true) => {
                    return nums[left as usize];
                }
                (true, false) => {
                    left = mid + 1;
                }
                (false, true) => {
                    right = mid;
                }
                (false, false) => {}
            }
        }

        i32::MIN
    }
}
// @lc code=end
