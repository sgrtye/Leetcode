/*
 * @lc app=leetcode id=79 lang=rust
 *
 * [79] Word Search
 */

// @lc code=start
impl Solution {
    fn dfs(
        board: &Vec<Vec<char>>,
        word: &Vec<char>,
        index: usize,
        visited: &mut Vec<Vec<bool>>,
        row: i32,
        col: i32,
    ) -> bool {
        if index == word.len() {
            return true;
        }

        if row < 0
            || col < 0
            || row >= board.len() as i32
            || col >= board[0].len() as i32
            || visited[row as usize][col as usize]
            || board[row as usize][col as usize] != word[index]
        {
            return false;
        }

        visited[row as usize][col as usize] = true;

        if Self::dfs(board, word, index + 1, visited, row + 1, col) {
            return true;
        }
        if Self::dfs(board, word, index + 1, visited, row - 1, col) {
            return true;
        }
        if Self::dfs(board, word, index + 1, visited, row, col + 1) {
            return true;
        }
        if Self::dfs(board, word, index + 1, visited, row, col - 1) {
            return true;
        }

        visited[row as usize][col as usize] = false;

        false
    }

    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let word: Vec<char> = word.chars().collect();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; board[0].len()]; board.len()];

        for i in 0..board.len() {
            for j in 0..board[0].len() {
                if Self::dfs(&board, &word, 0, &mut visited, i as i32, j as i32) {
                    return true;
                }
            }
        }

        false
    }
}
// @lc code=end
