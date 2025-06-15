/*
 * @lc app=leetcode id=295 lang=rust
 *
 * [295] Find Median from Data Stream
 */

// @lc code=start
use std::cmp::Ordering;
use std::collections::BinaryHeap;

struct MedianFinder {
    left: BinaryHeap<i32>,
    right: BinaryHeap<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {
    fn new() -> Self {
        MedianFinder {
            left: BinaryHeap::new(),
            right: BinaryHeap::new(),
        }
    }

    fn add_num(&mut self, num: i32) {
        match self.left.len().cmp(&self.right.len()) {
            Ordering::Equal => {
                if self.left.is_empty() || num < *self.left.peek().unwrap() {
                    self.left.push(num);
                } else {
                    self.right.push(-num);
                }
            }
            Ordering::Less => {
                self.right.push(-num);
                self.left.push(-self.right.pop().unwrap());
            }
            Ordering::Greater => {
                self.left.push(num);
                self.right.push(-self.left.pop().unwrap());
            }
        }
    }

    fn find_median(&self) -> f64 {
        match self.left.len().cmp(&self.right.len()) {
            Ordering::Equal => {
                let &num1 = self.left.peek().unwrap();
                let &num2 = self.right.peek().unwrap();

                (num1 - num2) as f64 / 2.0
            }
            Ordering::Less => -self.right.peek().unwrap() as f64,
            Ordering::Greater => *self.left.peek().unwrap() as f64,
        }
    }
}

// /**
//  * Your MedianFinder object will be instantiated and called as such:
//  * let obj = MedianFinder::new();
//  * obj.add_num(num);
//  * let ret_2: f64 = obj.find_median();
//  */
// @lc code=end
