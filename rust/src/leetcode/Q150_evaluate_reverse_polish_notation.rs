/*
 * @lc app=leetcode id=150 lang=rust
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = vec![];

        for t in tokens {
            match t.as_str() {
                "+" | "-" | "*" | "/" => {
                    let num2: i32 = stack.pop().unwrap();
                    let num1: i32 = stack.pop().unwrap();

                    let result: i32 = match t.as_str() {
                        "+" => num1 + num2,
                        "-" => num1 - num2,
                        "*" => num1 * num2,
                        "/" => num1 / num2,
                        _ => 0,
                    };

                    stack.push(result);
                }
                _ => {
                    let num: i32 = t.parse().unwrap();
                    stack.push(num);
                }
            }
        }

        stack.pop().unwrap()
    }
}
// @lc code=end
