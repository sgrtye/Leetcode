/*
 * @lc app=leetcode id=39 lang=rust
 *
 * [39] Combination Sum
 */

// @lc code=start
impl Solution {
    fn backtrack(
        candidates: &Vec<i32>,
        target: i32,
        current: &mut Vec<i32>,
        value: i32,
        result: &mut Vec<Vec<i32>>,
        index: usize,
    ) {
        if value == target {
            result.push(current.clone());
            return;
        } else if value > target || index == candidates.len() {
            return;
        }

        current.push(candidates[index]);
        Self::backtrack(
            candidates,
            target,
            current,
            value + candidates[index],
            result,
            index,
        );

        current.pop();
        Self::backtrack(candidates, target, current, value, result, index + 1);
    }

    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];
        let mut current: Vec<i32> = vec![];

        Self::backtrack(&candidates, target, &mut current, 0, &mut result, 0);

        result
    }
}
// @lc code=end
