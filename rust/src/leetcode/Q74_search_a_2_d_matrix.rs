/*
 * @lc app=leetcode id=74 lang=rust
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let rows: i32 = matrix.len() as i32;
        let cols: i32 = matrix[0].len() as i32;

        let mut left: i32 = 0;
        let mut right: i32 = rows * cols - 1;

        while left <= right {
            let mid: i32 = left + ((right - left) / 2);
            let value: i32 = matrix[(mid / cols) as usize][(mid % cols) as usize];

            if value == target {
                return true;
            }

            if value < target {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        false
    }
}
// @lc code=end
