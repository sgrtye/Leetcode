/*
 * @lc app=leetcode id=973 lang=rust
 *
 * [973] K Closest Points to Origin
 */

// @lc code=start
use std::collections::BinaryHeap;

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut heap: BinaryHeap<(i32, Vec<i32>)> = BinaryHeap::new();

        for point in points {
            let x: i32 = point[0];
            let y: i32 = point[1];
            let distance_squared: i32 = x * x + y * y;

            if heap.len() < k as usize {
                heap.push((distance_squared, point));
            } else if distance_squared < heap.peek().unwrap().0 {
                heap.pop();
                heap.push((distance_squared, point));
            }
        }

        heap.into_iter().map(|(_, point)| point).collect()
    }
}
// @lc code=end
