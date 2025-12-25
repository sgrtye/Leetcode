/*
 * @lc app=leetcode id=703 lang=rust
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct KthLargest {
    heap: BinaryHeap<Reverse<i32>>,
    capacity: usize,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut heap: BinaryHeap<Reverse<i32>> = nums.into_iter().map(Reverse).collect();
        while heap.len() > k as usize {
            heap.pop();
        }

        KthLargest {
            heap,
            capacity: k as usize,
        }
    }

    fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));

        if self.heap.len() > self.capacity {
            self.heap.pop();
        }

        self.heap.peek().unwrap().0
    }
}

// /**
//  * Your KthLargest object will be instantiated and called as such:
//  * let obj = KthLargest::new(k, nums);
//  * let ret_1: i32 = obj.add(val);
//  */
// @lc code=end
