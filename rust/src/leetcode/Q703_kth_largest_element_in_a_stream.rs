/*
 * @lc app=leetcode id=703 lang=rust
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
use std::collections::BinaryHeap;

struct KthLargest {
    heap: BinaryHeap<i32>,
    capacity: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut heap: BinaryHeap<i32> = nums.into_iter().map(|x| -x).collect();
        while heap.len() > k as usize {
            heap.pop();
        }

        KthLargest { heap, capacity: k }
    }

    fn add(&mut self, val: i32) -> i32 {
        self.heap.push(-val);

        if self.heap.len() > self.capacity as usize {
            self.heap.pop();
        }

        -self.heap.peek().unwrap()
    }
}

// /**
//  * Your KthLargest object will be instantiated and called as such:
//  * let obj = KthLargest::new(k, nums);
//  * let ret_1: i32 = obj.add(val);
//  */
// @lc code=end
