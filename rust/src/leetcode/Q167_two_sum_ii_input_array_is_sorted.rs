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

        let mut current: i32 = numbers[left] + numbers[right];

        while current != target {
            if current < target {
                left += 1;
            } else {
                right -= 1;
            }

            current = numbers[left] + numbers[right];
        }

        vec![left as i32 + 1, right as i32 + 1]
    }
}
// @lc code=end
