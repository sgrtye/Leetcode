/*
 * @lc app=leetcode id=36 lang=rust
 *
 * [36] Valid Sudoku
 */

// @lc code=start
use std::array;
use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut sets: [HashSet<char>; 27] = array::from_fn(|_| HashSet::new());

        for i in 0..9 {
            for j in 0..9 {
                let num: char = board[i][j];
                if num == '.' {
                    continue;
                }

                if !sets[i].insert(num) {
                    return false;
                }

                if !sets[j + 9].insert(num) {
                    return false;
                }

                if !sets[(i / 3) * 3 + (j / 3) + 18].insert(num) {
                    return false;
                }
            }
        }

        true
    }
}
// @lc code=end
