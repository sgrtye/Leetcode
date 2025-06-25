/*
 * @lc app=leetcode id=295 lang=rust
 *
 * [295] Find Median from Data Stream
 */

// @lc code=start
use std::cmp::Ordering;
use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct MedianFinder {
    left: BinaryHeap<i32>,
    right: BinaryHeap<Reverse<i32>>,
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
                    self.right.push(Reverse(num));
                }
            }
            Ordering::Less => {
                self.right.push(Reverse(num));
                if let Some(Reverse(min_val)) = self.right.pop() {
                    self.left.push(min_val);
                }
            }
            Ordering::Greater => {
                self.left.push(num);
                if let Some(max_val) = self.left.pop() {
                    self.right.push(Reverse(max_val));
                }
            }
        }
    }

    fn find_median(&self) -> f64 {
        match self.left.len().cmp(&self.right.len()) {
            Ordering::Less => self.right.peek().unwrap().0 as f64,
            Ordering::Greater => *self.left.peek().unwrap() as f64,
            Ordering::Equal => {
                let &max_left = self.left.peek().unwrap();
                let &Reverse(min_right) = self.right.peek().unwrap();

                (max_left + min_right) as f64 / 2.0
            }
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
