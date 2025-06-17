/*
 * @lc app=leetcode id=130 lang=rust
 *
 * [130] Surrounded Regions
 */

// @lc code=start
impl Solution {
    fn dfs(board: &mut Vec<Vec<char>>, row: i32, col: i32) {
        static DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        if board[row as usize][col as usize] != 'O' {
            return;
        }

        board[row as usize][col as usize] = 'T';

        for (dx, dy) in DIRECTIONS {
            let new_row: i32 = row + dx;
            let new_col: i32 = col + dy;

            if new_row >= 0
                && new_col >= 0
                && new_row < board.len() as i32
                && new_col < board[0].len() as i32
            {
                Self::dfs(board, new_row, new_col);
            }
        }
    }

    pub fn solve(board: &mut Vec<Vec<char>>) {
        let rows: usize = board.len();
        let cols: usize = board[0].len();

        for row in 0..rows {
            Self::dfs(board, row as i32, 0);
            Self::dfs(board, row as i32, cols as i32 - 1);
        }

        for col in 0..cols {
            Self::dfs(board, 0, col as i32);
            Self::dfs(board, rows as i32 - 1, col as i32);
        }

        for row in 0..rows {
            for col in 0..cols {
                match board[row][col] {
                    'T' => {
                        board[row][col] = 'O';
                    }
                    'O' => {
                        board[row][col] = 'X';
                    }
                    _ => {}
                }
            }
        }
    }
}
// @lc code=end
