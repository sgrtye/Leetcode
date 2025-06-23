/*
 * @lc app=leetcode id=190 lang=rust
 *
 * [190] Reverse Bits
 */

// @lc code=start
impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut x: u32 = x;
        let mut result: u32 = 0;

        for _ in 0..32 {
            result <<= 1;
            result |= x & 1;
            x >>= 1;
        }

        result
    }
}
// @lc code=end

