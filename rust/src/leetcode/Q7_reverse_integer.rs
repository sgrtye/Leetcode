/*
 * @lc app=leetcode id=7 lang=rust
 *
 * [7] Reverse Integer
 */

// @lc code=start
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut num = x;
        let mut result = 0i32;

        while num != 0 {
            if !(i32::MIN / 10..=i32::MAX / 10).contains(&result) {
                return 0;
            }

            let digit = num % 10;

            if result == i32::MAX / 10 && digit > 7 {
                return 0;
            }

            if result == i32::MIN / 10 && digit < -8 {
                return 0;
            }

            result = result * 10 + digit;
            num /= 10;
        }

        result
    }
}
// @lc code=end
