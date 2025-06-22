/*
 * @lc app=leetcode id=322 lang=rust
 *
 * [322] Coin Change
 */

// @lc code=start
impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut result: Vec<i32> = vec![i32::MAX; amount as usize + 1];
        result[0] = 0;

        for i in 1..result.len() {
            for &c in &coins {
                if i as i32 - c >= 0 && result[i - c as usize] != i32::MAX {
                    result[i] = result[i].min(result[i - c as usize] + 1);
                }
            }
        }

        if result[amount as usize] != i32::MAX {
            result[amount as usize]
        } else {
            -1
        }
    }
}
// @lc code=end
