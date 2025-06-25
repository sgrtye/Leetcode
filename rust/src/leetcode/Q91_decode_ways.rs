/*
 * @lc app=leetcode id=91 lang=rust
 *
 * [91] Decode Ways
 */

// @lc code=start
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let n: usize = chars.len();

        if n == 1 {
            return if chars[0] == '0' { 0 } else { 1 };
        }

        let mut dp: Vec<i32> = vec![0; n];
        dp[0] = if chars[0] == '0' { 0 } else { 1 };

        if chars[1] != '0' {
            dp[1] += dp[0];
        }

        let first_two: i32 = format!("{}{}", chars[0], chars[1]).parse::<i32>().unwrap();
        if (10..=26).contains(&first_two) {
            dp[1] += 1;
        }

        for i in 2..n {
            let char = chars[i];
            let previous_one: bool = chars[i - 1] == '1';
            let previous_two: bool = chars[i - 1] == '2';

            match char {
                '0' => {
                    if !(previous_one || previous_two) {
                        return 0;
                    }
                    dp[i] = dp[i - 2];
                }
                '1' | '2' | '3' | '4' | '5' | '6' => {
                    if previous_one || previous_two {
                        dp[i] = dp[i - 1] + dp[i - 2];
                    } else {
                        dp[i] = dp[i - 1];
                    }
                }
                '7' | '8' | '9' => {
                    if previous_one {
                        dp[i] = dp[i - 1] + dp[i - 2];
                    } else {
                        dp[i] = dp[i - 1];
                    }
                }
                _ => return 0,
            }
        }

        dp[n - 1]
    }
}
// @lc code=end
