/*
 * @lc app=leetcode id=33 lang=rust
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left: i32 = 0;
        let mut right: i32 = nums.len() as i32 - 1;

        while left <= right {
            let mid: i32 = left + ((right - left) / 2);

            let mid_num: i32 = nums[mid as usize];
            if mid_num == target {
                return mid;
            }

            let left_num: i32 = nums[left as usize];
            let right_num: i32 = nums[right as usize];

            // Left sorted
            if left_num <= mid_num {
                if left_num <= target && target <= mid_num {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            // Right sorted
            if mid_num <= right_num {
                if mid_num <= target && target <= right_num {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        -1
    }
}
// @lc code=end
