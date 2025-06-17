/*
 * @lc app=leetcode id=46 lang=rust
 *
 * [46] Permutations
 */

// @lc code=start
impl Solution {
    fn backtrack(
        nums: &Vec<i32>,
        included: &mut Vec<bool>,
        current: &mut Vec<i32>,
        reamined: usize,
        result: &mut Vec<Vec<i32>>,
    ) {
        if reamined == 0 {
            result.push(current.clone());
            return;
        }

        for i in 0..nums.len() {
            if !included[i] {
                included[i] = true;
                current.push(nums[i]);

                Self::backtrack(nums, included, current, reamined - 1, result);

                included[i] = false;
                current.pop();
            }
        }
    }

    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut current: Vec<i32> = Vec::new();
        let mut included: Vec<bool> = vec![false; nums.len()];

        Self::backtrack(&nums, &mut included, &mut current, nums.len(), &mut result);

        result
    }
}
// @lc code=end
