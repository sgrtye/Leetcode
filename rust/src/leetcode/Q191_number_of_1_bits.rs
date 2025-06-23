/*
 * @lc app=leetcode id=191 lang=rust
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        let mut result: i32 = 0;
        let mut number: i32 = n;

        while number != 0 {
            result += number & 1;
            number >>= 1;
        }

        result
    }
}
// @lc code=end
