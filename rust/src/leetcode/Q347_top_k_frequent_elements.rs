/*
 * @lc app=leetcode id=347 lang=rust
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
use std::collections::BinaryHeap;
use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut counts: HashMap<i32, i32> = HashMap::new();

        for n in nums {
            *counts.entry(n).or_insert(0) += 1;
        }

        let mut frequency_heap: BinaryHeap<(i32, i32)> = BinaryHeap::new();

        for (num, frequency) in counts {
            frequency_heap.push((frequency, num));
        }

        let mut result: Vec<i32> = vec![];

        for _ in 0..k {
            if let Some((_, num)) = frequency_heap.pop() {
                result.push(num);
            }
        }

        result
    }
}
// @lc code=end
