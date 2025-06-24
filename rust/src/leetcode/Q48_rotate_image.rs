/*
 * @lc app=leetcode id=48 lang=rust
 *
 * [48] Rotate Image
 */

// @lc code=start
impl Solution {
    fn rotate_layer(matrix: &mut Vec<Vec<i32>>, left: usize, right: usize) {
        for i in 0..right - left {
            let value: i32 = matrix[left][left + i];

            matrix[left][left + i] = matrix[right - i][left];
            matrix[right - i][left] = matrix[right][right - i];
            matrix[right][right - i] = matrix[left + i][right];
            matrix[left + i][right] = value;
        }
    }

    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let mut left: usize = 0;
        let mut right: usize = matrix.len() - 1;

        while left < right {
            Self::rotate_layer(matrix, left, right);
            left += 1;
            right -= 1;
        }
    }
}
// @lc code=end
