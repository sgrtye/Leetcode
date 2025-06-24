/*
 * @lc app=leetcode id=73 lang=rust
 *
 * [73] Set Matrix Zeroes
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let rows: usize = matrix.len();
        let cols: usize = matrix[0].len();

        let mut marked_rows: HashSet<usize> = HashSet::new();
        let mut marked_cols: HashSet<usize> = HashSet::new();

        for i in 0..rows {
            for j in 0..cols {
                if matrix[i][j] == 0 {
                    marked_rows.insert(i);
                    marked_cols.insert(j);
                }
            }
        }

        for i in marked_rows {
            for j in 0..cols {
                matrix[i][j] = 0;
            }
        }

        for j in marked_cols {
            for i in 0..rows {
                matrix[i][j] = 0;
            }
        }
    }
}
// @lc code=end
