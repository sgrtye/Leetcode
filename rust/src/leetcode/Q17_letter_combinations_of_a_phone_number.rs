/*
 * @lc app=leetcode id=17 lang=rust
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
impl Solution {
    fn backtrack(
        digits: &Vec<usize>,
        mapping: &[&[char]],
        index: usize,
        current: &mut Vec<char>,
        result: &mut Vec<String>,
    ) {
        if index == digits.len() {
            result.push(current.iter().collect());
            return;
        }

        for &c in mapping[digits[index]] {
            current.push(c);

            Self::backtrack(digits, mapping, index + 1, current, result);

            current.pop();
        }
    }

    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return Vec::new();
        }

        let mapping: [&[char]; 10] = [
            &[],                   // 0
            &[],                   // 1
            &['a', 'b', 'c'],      // 2
            &['d', 'e', 'f'],      // 3
            &['g', 'h', 'i'],      // 4
            &['j', 'k', 'l'],      // 5
            &['m', 'n', 'o'],      // 6
            &['p', 'q', 'r', 's'], // 7
            &['t', 'u', 'v'],      // 8
            &['w', 'x', 'y', 'z'], // 9
        ];

        let digits: Vec<usize> = digits
            .chars()
            .map(|d| d.to_digit(10).unwrap() as usize)
            .collect();
        let mut current: Vec<char> = Vec::new();
        let mut result: Vec<String> = Vec::new();

        Self::backtrack(&digits, &mapping, 0, &mut current, &mut result);

        result
    }
}
// @lc code=end
