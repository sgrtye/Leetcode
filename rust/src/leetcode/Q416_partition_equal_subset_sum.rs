/*
 * @lc app=leetcode id=416 lang=rust
 *
 * [416] Partition Equal Subset Sum
 */

// @lc code=start
impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let sum: i32 = nums.iter().sum::<i32>();

        if sum % 2 != 0 {
            return false;
        }

        let target: i32 = sum / 2;
        let mut dp: Vec<bool> = vec![false; target as usize + 1];
        dp[0] = true;

        for &num in &nums {
            for i in (num as usize..=target as usize).rev() {
                dp[i] = dp[i] || dp[i - num as usize];
            }
        }

        dp[dp.len() - 1]
    }
}
// @lc code=end
