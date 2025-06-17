/*
 * @lc app=leetcode id=90 lang=rust
 *
 * [90] Subsets II
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
        let mut new_index: usize = index;
        let candidate: i32 = nums[index];
        while new_index < nums.len() && nums[new_index] == candidate {
            new_index += 1;
        }
        Self::backtrack(nums, current, result, new_index);
    }

    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut sorted_nums: Vec<i32> = nums;
        sorted_nums.sort();

        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut current: Vec<i32> = Vec::new();

        Self::backtrack(&sorted_nums, &mut current, &mut result, 0);

        result
    }
}
// @lc code=end
