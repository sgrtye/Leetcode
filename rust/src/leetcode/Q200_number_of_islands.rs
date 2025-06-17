/*
 * @lc app=leetcode id=200 lang=rust
 *
 * [200] Number of Islands
 */

// @lc code=start
impl Solution {
    fn dfs(row: i32, col: i32, grid: &mut Vec<Vec<char>>) -> bool {
        if row < 0
            || col < 0
            || row >= grid.len() as i32
            || col >= grid[0].len() as i32
            || grid[row as usize][col as usize] == '0'
        {
            return false;
        }

        grid[row as usize][col as usize] = '0';

        Self::dfs(row - 1, col, grid);
        Self::dfs(row + 1, col, grid);
        Self::dfs(row, col - 1, grid);
        Self::dfs(row, col + 1, grid);

        true
    }

    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut result: i32 = 0;
        let mut grid: Vec<Vec<char>> = grid;

        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if Self::dfs(i as i32, j as i32, &mut grid) {
                    result += 1;
                }
            }
        }

        result
    }
}
// @lc code=end
