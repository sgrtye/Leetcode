/*
 * @lc app=leetcode id=43 lang=rust
 *
 * [43] Multiply Strings
 */

// @lc code=start
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }

        let num1: Vec<u32> = num1
            .chars()
            .rev()
            .map(|c| c.to_digit(10).unwrap())
            .collect();
        let num2: Vec<u32> = num2
            .chars()
            .rev()
            .map(|c| c.to_digit(10).unwrap())
            .collect();

        let mut result = vec![0; num1.len() + num2.len()];

        for i in 0..num1.len() {
            for j in 0..num2.len() {
                let mul: u32 = num1[i] * num2[j];
                result[i + j] += mul;

                if result[i + j] >= 10 {
                    result[i + j + 1] += result[i + j] / 10;
                    result[i + j] %= 10;
                }
            }
        }

        result
            .iter()
            .rev()
            .skip_while(|&&x| x == 0)
            .map(|&x| char::from_digit(x, 10).unwrap())
            .collect()
    }
}
// @lc code=end
