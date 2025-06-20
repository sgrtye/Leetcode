/*
 * @lc app=leetcode id=678 lang=rust
 *
 * [678] Valid Parenthesis String
 */

// @lc code=start
impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut left_min: i32 = 0;
        let mut left_max: i32 = 0;

        for c in s.chars() {
            match c {
                '(' => {
                    left_min += 1;
                    left_max += 1;
                }
                ')' => {
                    left_min -= 1;
                    left_max -= 1;
                }
                '*' => {
                    left_min -= 1;
                    left_max += 1;
                }
                _ => {}
            }

            if left_max < 0 {
                return false;
            }

            if left_min < 0 {
                left_min = 0;
            }
        }

        left_min == 0
    }
}
// @lc code=end
