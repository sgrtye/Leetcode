/*
 * @lc app=leetcode id=4 lang=rust
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
use std::cmp::{max, min};

impl Solution {
    fn order_list_by_length(nums1: Vec<i32>, nums2: Vec<i32>) -> (Vec<i32>, Vec<i32>) {
        if nums1.len() <= nums2.len() {
            (nums1, nums2)
        } else {
            (nums2, nums1)
        }
    }

    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (shorter, longer) = Self::order_list_by_length(nums1, nums2);

        let half_length: i32 = (shorter.len() + longer.len()) as i32 / 2;

        let mut left: i32 = 0;
        let mut right: i32 = shorter.len() as i32;

        while left <= right {
            let shorter_mid: i32 = left + (right - left) / 2;
            let longer_mid: i32 = half_length - shorter_mid;

            let shorter_left: i32 = if shorter_mid != 0 {
                shorter[shorter_mid as usize - 1]
            } else {
                i32::MIN
            };
            let shorter_right: i32 = if shorter_mid != shorter.len() as i32 {
                shorter[shorter_mid as usize]
            } else {
                i32::MAX
            };
            let longer_left: i32 = if longer_mid != 0 {
                longer[longer_mid as usize - 1]
            } else {
                i32::MIN
            };
            let longer_right: i32 = if longer_mid != longer.len() as i32 {
                longer[longer_mid as usize]
            } else {
                i32::MAX
            };

            if shorter_left <= longer_right && longer_left <= shorter_right {
                if (shorter.len() + longer.len()) % 2 == 1 {
                    return min(shorter_right, longer_right) as f64;
                } else {
                    let median_left: i32 = max(shorter_left, longer_left);
                    let median_right: i32 = min(shorter_right, longer_right);

                    return (median_left + median_right) as f64 / 2.0;
                }
            }

            if shorter_left > longer_right {
                right = shorter_mid - 1;
            } else {
                left = shorter_mid + 1;
            }
        }

        0.0
    }
}
// @lc code=end
