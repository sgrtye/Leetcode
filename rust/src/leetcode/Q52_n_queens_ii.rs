/*
 * @lc app=leetcode id=52 lang=rust
 *
 * [52] N-Queens II
 */

// @lc code=start
impl Solution {
    fn backtrack(
        n: usize,
        row: usize,
        cols: &mut Vec<bool>,
        pos_diag: &mut Vec<bool>,
        neg_diag: &mut Vec<bool>,
        result: &mut i32,
    ) {
        if row == n {
            *result += 1;
            return;
        }

        for col in 0..n {
            if cols[col] || pos_diag[row + col] || neg_diag[row - col + n - 1] {
                continue;
            }

            cols[col] = true;
            pos_diag[row + col] = true;
            neg_diag[row - col + n - 1] = true;

            Self::backtrack(n, row + 1, cols, pos_diag, neg_diag, result);

            cols[col] = false;
            pos_diag[row + col] = false;
            neg_diag[row - col + n - 1] = false;
        }
    }

    pub fn total_n_queens(n: i32) -> i32 {
        let mut result: i32 = 0;

        let mut cols: Vec<bool> = vec![false; n as usize];
        let mut pos_diag: Vec<bool> = vec![false; 2 * n as usize - 1];
        let mut neg_diag: Vec<bool> = vec![false; 2 * n as usize - 1];

        Self::backtrack(
            n as usize,
            0,
            &mut cols,
            &mut pos_diag,
            &mut neg_diag,
            &mut result,
        );

        result
    }
}
// @lc code=end
