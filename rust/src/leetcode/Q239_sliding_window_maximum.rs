/*
 * @lc app=leetcode id=239 lang=rust
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut deque: VecDeque<(usize, i32)> = VecDeque::new();
        let mut result: Vec<i32> = vec![0; nums.len() - k as usize + 1];

        for right in 0..nums.len() {
            let right_value: i32 = nums[right];

            while let Some(&(_, value)) = deque.back() {
                if value < right_value {
                    deque.pop_back();
                } else {
                    break;
                }
            }

            if let Some(&(index, _)) = deque.front() {
                if (index as i32) < (right as i32) - k + 1 {
                    deque.pop_front();
                }
            }

            deque.push_back((right, right_value));

            if right + 1 >= k as usize {
                result[right - k as usize + 1] = deque.front().unwrap().1;
            }
        }

        result
    }
}
// @lc code=end
