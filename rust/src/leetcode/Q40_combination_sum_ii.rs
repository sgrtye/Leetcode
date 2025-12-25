/*
 * @lc app=leetcode id=40 lang=rust
 *
 * [40] Combination Sum II
 */

// @lc code=start
struct Solver {
    candidates: Vec<i32>,
    target: i32,
    result: Vec<Vec<i32>>,
}

impl Solver {
    fn new(candidates: Vec<i32>, target: i32) -> Self {
        let mut candidates = candidates;
        candidates.sort();

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
        self.backtrack(current, value + self.candidates[index], index + 1);

        current.pop();

        let v = self.candidates[index];
        let mut new_index = index;
        while new_index < self.candidates.len() && self.candidates[new_index] == v {
            new_index += 1;
        }

        self.backtrack(current, value, new_index);
    }

    fn solve(&mut self) {
        self.backtrack(&mut vec![], 0, 0);
    }
}

impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut solver = Solver::new(candidates, target);
        solver.solve();
        solver.result
    }
}
// @lc code=end
