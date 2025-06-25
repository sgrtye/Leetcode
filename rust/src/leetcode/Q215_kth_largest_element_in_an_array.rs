/*
 * @lc app=leetcode id=215 lang=rust
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let k: usize = k as usize;
        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::with_capacity(k);

        for &n in nums.iter() {
            if heap.len() < k {
                heap.push(Reverse(n));
            } else if n > heap.peek().unwrap().0 {
                heap.pop();
                heap.push(Reverse(n));
            }
        }

        heap.peek().unwrap().0
    }
}
// @lc code=end
