/*
 * @lc app=leetcode id=78 lang=rust
 *
 * [78] Subsets
 */

// @lc code=start
impl Solution {
    fn backtrack(
        nums: &Vec<i32>,
        current: &mut Vec<i32>,
        result: &mut Vec<Vec<i32>>,
        index: usize,
    ) {
        if index == nums.len() {
            result.push(current.clone());
            return;
        }

        current.push(nums[index]);
        Self::backtrack(nums, current, result, index + 1);

        current.pop();
        Self::backtrack(nums, current, result, index + 1);
    }

    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];
        let mut current: Vec<i32> = vec![];

        Self::backtrack(&nums, &mut current, &mut result, 0);

        result
    }
}
// @lc code=end
