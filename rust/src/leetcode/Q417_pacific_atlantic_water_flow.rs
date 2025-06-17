/*
 * @lc app=leetcode id=417 lang=rust
 *
 * [417] Pacific Atlantic Water Flow
 */

// @lc code=start
impl Solution {
    fn flood(heights: &Vec<Vec<i32>>, map: &mut Vec<Vec<bool>>, row: i32, col: i32) {
        static DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        map[row as usize][col as usize] = true;
        let height: i32 = heights[row as usize][col as usize];

        for (dx, dy) in DIRECTIONS {
            let new_row: i32 = row + dx;
            let new_col: i32 = col + dy;

            if new_row >= 0
                && new_col >= 0
                && new_row < heights.len() as i32
                && new_col < heights[0].len() as i32
                && !map[new_row as usize][new_col as usize]
                && height <= heights[new_row as usize][new_col as usize]
            {
                Self::flood(heights, map, new_row, new_col);
            }
        }
    }

    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows: usize = heights.len();
        let cols: usize = heights[0].len();
        let mut pacific_map: Vec<Vec<bool>> = vec![vec![false; cols]; rows];
        let mut atlantic_map: Vec<Vec<bool>> = vec![vec![false; cols]; rows];

        for row in 0..rows {
            Self::flood(&heights, &mut pacific_map, row as i32, 0);
            Self::flood(&heights, &mut atlantic_map, row as i32, cols as i32 - 1);
        }

        for col in 0..cols {
            Self::flood(&heights, &mut pacific_map, 0, col as i32);
            Self::flood(&heights, &mut atlantic_map, rows as i32 - 1, col as i32);
        }

        let mut result: Vec<Vec<i32>> = Vec::new();

        for row in 0..rows {
            for col in 0..cols {
                if pacific_map[row][col] && atlantic_map[row][col] {
                    result.push(vec![row as i32, col as i32]);
                }
            }
        }

        result
    }
}
// @lc code=end
