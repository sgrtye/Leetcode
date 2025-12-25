/*
 * @lc app=leetcode id=46 lang=rust
 *
 * [46] Permutations
 */

// @lc code=start
use std::collections::HashSet;

struct Solver {
    nums: HashSet<i32>,
    result: Vec<Vec<i32>>,
}

impl Solver {
    fn new(nums: Vec<i32>) -> Self {
        Solver {
            nums: nums.into_iter().collect(),
            result: Vec::new(),
        }
    }

    fn backtrack(&mut self, current: &mut Vec<i32>) {
        if self.nums.is_empty() {
            self.result.push(current.clone());
            return;
        }

        for n in self.nums.clone() {
            current.push(n);
            self.nums.remove(&n);

            self.backtrack(current);

            self.nums.insert(n);
            current.pop();
        }
    }

    fn solve(&mut self) {
        self.backtrack(&mut vec![]);
    }
}

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut solver = Solver::new(nums);
        solver.solve();
        solver.result
    }
}
// @lc code=end
