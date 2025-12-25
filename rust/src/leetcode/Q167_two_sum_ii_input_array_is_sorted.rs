/*
 * @lc app=leetcode id=167 lang=rust
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left: usize = 0;
        let mut right: usize = numbers.len() - 1;

        while left < right {
            let current: i32 = numbers[left] + numbers[right];

            if current < target {
                left += 1;
            } else if current > target {
                right -= 1;
            } else {
                return vec![left as i32 + 1, right as i32 + 1];
            }
        }

        vec![]
    }
}
// @lc code=end
