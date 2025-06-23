/*
 * @lc app=leetcode id=329 lang=rust
 *
 * [329] Longest Increasing Path in a Matrix
 */

// @lc code=start
impl Solution {
    fn dfs(
        matrix: &Vec<Vec<i32>>,
        dp: &mut Vec<Vec<i32>>,
        row: usize,
        col: usize,
        rows: usize,
        cols: usize,
    ) -> i32 {
        if dp[row][col] != -1 {
            return dp[row][col];
        }

        let mut result: i32 = 0;
        static DIRECTIONS: [(i32, i32); 4] = [(0, 1), (0, -1), (1, 0), (-1, 0)];

        for (dx, dy) in DIRECTIONS {
            let new_row: i32 = row as i32 + dx;
            let new_col: i32 = col as i32 + dy;

            if new_row >= 0 && new_row < rows as i32 && new_col >= 0 && new_col < cols as i32 {
                let new_row: usize = new_row as usize;
                let new_col: usize = new_col as usize;

                if matrix[row][col] < matrix[new_row][new_col] {
                    let new_max = Self::dfs(matrix, dp, new_row, new_col, rows, cols);
                    if new_max > result {
                        result = new_max;
                    }
                }
            }
        }

        dp[row][col] = result + 1;
        result + 1
    }

    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        let rows: usize = matrix.len();
        let cols: usize = matrix[0].len();
        let mut dp: Vec<Vec<i32>> = vec![vec![-1; cols]; rows];

        let mut result: i32 = 0;

        for i in 0..rows {
            for j in 0..cols {
                let new_max = Self::dfs(&matrix, &mut dp, i, j, rows, cols);

                if new_max > result {
                    result = new_max;
                }
            }
        }

        result
    }
}

// @lc code=end
