/*
 * @lc app=leetcode id=22 lang=rust
 *
 * [22] Generate Parentheses
 */

// @lc code=start
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        // (string, left_count, right_count)
        let mut stack: Vec<(String, i32, i32)> = vec![(String::new(), 0, 0)];

        while let Some((current, left, right)) = stack.pop() {
            if left == n && right == n {
                result.push(current);
                continue;
            }

            if left < n {
                stack.push((current.clone() + "(", left + 1, right));
            }

            if left > right {
                stack.push((current + ")", left, right + 1));
            }
        }

        result
    }
}
// @lc code=end
