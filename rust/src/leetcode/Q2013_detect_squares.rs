/*
 * @lc app=leetcode id=2013 lang=rust
 *
 * [2013] Detect Squares
 */

// @lc code=start
use std::collections::HashMap;

struct DetectSquares {
    points: HashMap<(i32, i32), i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DetectSquares {
    fn new() -> Self {
        Self {
            points: HashMap::new(),
        }
    }

    fn add(&mut self, point: Vec<i32>) {
        let key: (i32, i32) = (point[0], point[1]);
        *self.points.entry(key).or_insert(0) += 1;
    }

    fn count(&self, point: Vec<i32>) -> i32 {
        let x: i32 = point[0];
        let y: i32 = point[1];

        let mut result: i32 = 0;

        for (&(i, j), &count) in &self.points {
            if x == i || y == j || (x - i).abs() != (y - j).abs() {
                continue;
            }

            result += count
                * self.points.get(&(x, j)).unwrap_or(&0)
                * self.points.get(&(i, y)).unwrap_or(&0);
        }

        result
    }
}

// /**
//  * Your DetectSquares object will be instantiated and called as such:
//  * let obj = DetectSquares::new();
//  * obj.add(point);
//  * let ret_2: i32 = obj.count(point);
//  */
// @lc code=end
