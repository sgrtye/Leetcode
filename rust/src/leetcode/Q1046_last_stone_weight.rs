/*
 * @lc app=leetcode id=1046 lang=rust
 *
 * [1046] Last Stone Weight
 */

// @lc code=start
use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap: BinaryHeap<i32> = BinaryHeap::from(stones);

        while heap.len() > 1 {
            let stone1: i32 = heap.pop().unwrap();
            let stone2: i32 = heap.pop().unwrap();

            if stone1 != stone2 {
                heap.push(stone1 - stone2);
            }
        }

        if !heap.is_empty() {
            *heap.peek().unwrap()
        } else {
            0
        }
    }
}
// @lc code=end
