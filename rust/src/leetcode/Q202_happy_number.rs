/*
 * @lc app=leetcode id=202 lang=rust
 *
 * [202] Happy Number
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut n: i32 = n;
        let mut numbers: HashSet<i32> = HashSet::new();

        while !numbers.contains(&n) {
            if n == 1 {
                return true;
            }
            numbers.insert(n);

            let mut summation: Vec<i32> = Vec::new();
            while n != 0 {
                let digit: i32 = n % 10;
                n /= 10;
                summation.push(digit * digit);
            }

            n = summation.into_iter().sum();
        }

        false
    }
}
// @lc code=end
