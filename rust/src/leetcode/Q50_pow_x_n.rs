/*
 * @lc app=leetcode id=50 lang=rust
 *
 * [50] Pow(x, n)
 */

// @lc code=start
impl Solution {
    fn power(x: f64, n: i32) -> f64 {
        if x == 0.0 {
            return 0.0;
        }

        if n == 0 {
            return 1.0;
        }

        let result: f64 = Self::power(x * x, n / 2);

        if n % 2 == 0 {
            result
        } else {
            x * result
        }
    }

    pub fn my_pow(x: f64, n: i32) -> f64 {
        let result: f64 = Self::power(x, n.abs());

        if n > 0 {
            result
        } else {
            1.0 / result
        }
    }
}
// @lc code=end
