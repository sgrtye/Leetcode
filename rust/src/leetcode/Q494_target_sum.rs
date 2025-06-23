/*
 * @lc app=leetcode id=494 lang=rust
 *
 * [494] Target Sum
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        let mut possible_results: HashMap<i32, i32> = HashMap::new();
        possible_results.insert(0, 1);

        for num in nums {
            let mut new_results: HashMap<i32, i32> = HashMap::new();

            for (&total, &count) in &possible_results {
                *new_results.entry(total + num).or_insert(0) += count;
                *new_results.entry(total - num).or_insert(0) += count;
            }

            possible_results = new_results;
        }

        *possible_results.get(&target).unwrap_or(&0)
    }
}
// @lc code=end
