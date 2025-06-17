/*
 * @lc app=leetcode id=51 lang=rust
 *
 * [51] N-Queens
 */

// @lc code=start
impl Solution {
    fn backtrack(
        n: usize,
        row: usize,
        cols: &mut Vec<bool>,
        pos_diag: &mut Vec<bool>,
        neg_diag: &mut Vec<bool>,
        current: &mut Vec<(usize, usize)>,
        result: &mut Vec<Vec<String>>,
    ) {
        if row == n {
            let mut board: Vec<Vec<char>> = vec![vec!['.'; n]; n];
            for &(row, col) in current.iter() {
                board[row][col] = 'Q';
            }

            let board_strings: Vec<String> = board
                .into_iter()
                .map(|row| row.into_iter().collect())
                .collect();

            result.push(board_strings);
            return;
        }

        for col in 0..n {
            if cols[col] || pos_diag[row + col] || neg_diag[row - col + n - 1] {
                continue;
            }

            cols[col] = true;
            pos_diag[row + col] = true;
            neg_diag[row - col + n - 1] = true;

            current.push((row, col));
            Self::backtrack(n, row + 1, cols, pos_diag, neg_diag, current, result);
            current.pop();

            cols[col] = false;
            pos_diag[row + col] = false;
            neg_diag[row - col + n - 1] = false;
        }
    }

    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = Vec::new();
        let mut current: Vec<(usize, usize)> = Vec::new();

        let mut cols: Vec<bool> = vec![false; n as usize];
        let mut pos_diag: Vec<bool> = vec![false; 2 * n as usize - 1];
        let mut neg_diag: Vec<bool> = vec![false; 2 * n as usize - 1];

        Self::backtrack(
            n as usize,
            0,
            &mut cols,
            &mut pos_diag,
            &mut neg_diag,
            &mut current,
            &mut result,
        );

        result
    }
}
// @lc code=end
