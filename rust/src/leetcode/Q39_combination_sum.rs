/*
 * @lc app=leetcode id=39 lang=rust
 *
 * [39] Combination Sum
 */

// @lc code=start
struct Solver {
    candidates: Vec<i32>,
    target: i32,
    result: Vec<Vec<i32>>,
}

impl Solver {
    fn new(candidates: Vec<i32>, target: i32) -> Self {
        Solver {
            candidates,
            target,
            result: Vec::new(),
        }
    }

    fn backtrack(&mut self, current: &mut Vec<i32>, value: i32, index: usize) {
        if value == self.target {
            self.result.push(current.clone());
            return;
        } else if value > self.target || index == self.candidates.len() {
            return;
        }

        current.push(self.candidates[index]);
        self.backtrack(current, value + self.candidates[index], index);

        current.pop();
        self.backtrack(current, value, index + 1);
    }

    fn solve(&mut self) {
        self.backtrack(&mut vec![], 0, 0);
    }
}

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut solver = Solver::new(candidates, target);
        solver.solve();
        solver.result
    }
}
// @lc code=end
