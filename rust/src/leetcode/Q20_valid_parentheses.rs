/*
 * @lc app=leetcode id=20 lang=rust
 *
 * [20] Valid Parentheses
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = vec![];
        let mapping: HashMap<char, char> = HashMap::from([('(', ')'), ('[', ']'), ('{', '}')]);

        for c in s.chars() {
            if mapping.contains_key(&c) {
                stack.push(c);
                continue;
            }

            if let Some(value) = stack.pop() {
                if mapping.get(&value) != Some(&c) {
                    return false;
                }
            } else {
                return false;
            }
        }

        stack.is_empty()
    }
}
// @lc code=end
