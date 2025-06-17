/*
 * @lc app=leetcode id=40 lang=rust
 *
 * [40] Combination Sum II
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
            index + 1,
        );

        current.pop();
        let mut new_index: usize = index;
        let candidate: i32 = candidates[index];
        while new_index < candidates.len() && candidates[new_index] == candidate {
            new_index += 1;
        }
        Self::backtrack(candidates, target, current, value, result, new_index);
    }

    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];
        let mut current: Vec<i32> = vec![];

        let mut sorted_candidates: Vec<i32> = candidates;
        sorted_candidates.sort();

        Self::backtrack(&sorted_candidates, target, &mut current, 0, &mut result, 0);

        result
    }
}
// @lc code=end
