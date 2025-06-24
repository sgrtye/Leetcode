/*
 * @lc app=leetcode id=54 lang=rust
 *
 * [54] Spiral Matrix
 */

// @lc code=start
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let rows: usize = matrix.len();
        let cols: usize = matrix[0].len();

        let mut result: Vec<i32> = Vec::new();
        let mut visited: Vec<Vec<bool>> = vec![vec![false; cols]; rows];

        let mut row: usize = 0;
        let mut col: usize = 0;

        let mut direction: usize = 0;
        static DIRECTIONS: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];

        for _ in 0..(rows * cols) {
            result.push(matrix[row][col]);
            visited[row][col] = true;

            let new_row: i32 = row as i32 + DIRECTIONS[direction].0;
            let new_col: i32 = col as i32 + DIRECTIONS[direction].1;

            if new_row < 0
                || new_row >= rows as i32
                || new_col < 0
                || new_col >= cols as i32
                || visited[new_row as usize][new_col as usize]
            {
                direction = (direction + 1) % 4;
                row = (row as i32 + DIRECTIONS[direction].0) as usize;
                col = (col as i32 + DIRECTIONS[direction].1) as usize;
            } else {
                row = new_row as usize;
                col = new_col as usize;
            }
        }

        result
    }
}
// @lc code=end
