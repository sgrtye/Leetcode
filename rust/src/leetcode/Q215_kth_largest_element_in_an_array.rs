/*
 * @lc app=leetcode id=215 lang=rust
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let k: usize = k as usize;
        let mut heap: BinaryHeap<i32> = BinaryHeap::new();

        for &n in nums.iter() {
            if heap.len() < k {
                heap.push(-n);
            } else if -n < *heap.peek().unwrap() {
                heap.pop();
                heap.push(-n);
            }
        }

        -heap.peek().unwrap()
    }
}
// @lc code=end
