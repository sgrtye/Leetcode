/*
 * @lc app=leetcode id=15 lang=rust
 *
 * [15] 3Sum
 */

// @lc code=start
use std::cmp::Ordering;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();

        let mut result: Vec<Vec<i32>> = vec![];

        for i in 0..nums.len().saturating_sub(2) {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let mut j: usize = i + 1;
            let mut k: usize = nums.len() - 1;

            while j < k {
                let current: i32 = nums[i] + nums[j] + nums[k];

                match current.cmp(&0) {
                    Ordering::Less => {
                        j += 1;
                    }
                    Ordering::Greater => {
                        k -= 1;
                    }
                    Ordering::Equal => {
                        result.push(vec![nums[i], nums[j], nums[k]]);

                        j += 1;
                        k -= 1;

                        while j < k && nums[j] == nums[j - 1] {
                            j += 1;
                        }
                    }
                }
            }
        }

        result
    }
}
// @lc code=end
