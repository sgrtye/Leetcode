/*
 * @lc app=leetcode id=973 lang=rust
 *
 * [973] K Closest Points to Origin
 */

// @lc code=start
use std::collections::BinaryHeap;

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let k: usize = k as usize;
        let mut heap: BinaryHeap<(i32, (i32, i32))> = BinaryHeap::new();

        for (index, point) in points.iter().enumerate() {
            let x = point[0];
            let y = point[1];
            let distance = x * x + y * y;

            heap.push((distance, (x, y)));

            if index >= k {
                heap.pop();
            }
        }

        heap.into_iter().map(|(_, (x, y))| vec![x, y]).collect()
    }
}
// @lc code=end
