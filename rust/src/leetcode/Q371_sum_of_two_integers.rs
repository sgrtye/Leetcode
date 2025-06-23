/*
 * @lc app=leetcode id=371 lang=rust
 *
 * [371] Sum of Two Integers
 */

// @lc code=start
impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        let mut a: i32 = a;
        let mut b: i32 = b;
        let mut result: i32 = 0;
        let mut carry: bool = false;
        let mut mask: i32 = 1;

        for _ in 0..32 {
            let bit_a: i32 = a & 1;
            let bit_b: i32 = b & 1;
            let carry_bit: i32 = if carry { 1 } else { 0 };

            let sum_bit: i32 = bit_a ^ bit_b ^ carry_bit;

            if sum_bit == 1 {
                result |= mask;
            }

            carry = (bit_a & bit_b) == 1 || (bit_a & carry_bit) == 1 || (bit_b & carry_bit) == 1;

            a >>= 1;
            b >>= 1;
            mask <<= 1;
        }

        result
    }
}
// @lc code=end
