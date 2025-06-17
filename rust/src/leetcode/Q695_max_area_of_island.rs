/*
 * @lc app=leetcode id=695 lang=rust
 *
 * [695] Max Area of Island
 */

// @lc code=start
impl Solution {
    fn dfs(row: i32, col: i32, grid: &mut Vec<Vec<i32>>) -> i32 {
        if row < 0
            || col < 0
            || row >= grid.len() as i32
            || col >= grid[0].len() as i32
            || grid[row as usize][col as usize] == 0
        {
            return 0;
        }

        let mut size: i32 = 1;
        grid[row as usize][col as usize] = 0;

        size += Self::dfs(row - 1, col, grid);
        size += Self::dfs(row + 1, col, grid);
        size += Self::dfs(row, col - 1, grid);
        size += Self::dfs(row, col + 1, grid);

        size
    }

    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let mut result: i32 = 0;
        let mut grid: Vec<Vec<i32>> = grid;

        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                let size: i32 = Self::dfs(i as i32, j as i32, &mut grid);

                if size > result {
                    result = size;
                }
            }
        }

        result
    }
}
// @lc code=end
