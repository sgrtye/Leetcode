/*
 * @lc app=leetcode id=78 lang=rust
 *
 * [78] Subsets
 */

// @lc code=start
struct Solver {
    nums: Vec<i32>,
    result: Vec<Vec<i32>>,
}

impl Solver {
    fn new(nums: Vec<i32>) -> Self {
        Solver {
            nums,
            result: Vec::new(),
        }
    }

    fn backtrack(&mut self, current: &mut Vec<i32>, index: usize) {
        if index == self.nums.len() {
            self.result.push(current.clone());
            return;
        }

        current.push(self.nums[index]);
        self.backtrack(current, index + 1);

        current.pop();
        self.backtrack(current, index + 1);
    }

    fn solve(&mut self) {
        self.backtrack(&mut vec![], 0);
    }
}

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut solver = Solver::new(nums);
        solver.solve();
        solver.result
    }
}
// @lc code=end
