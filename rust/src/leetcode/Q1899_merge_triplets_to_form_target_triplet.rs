/*
 * @lc app=leetcode id=1899 lang=rust
 *
 * [1899] Merge Triplets to Form Target Triplet
 */

// @lc code=start
impl Solution {
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let mut x: bool = false;
        let mut y: bool = false;
        let mut z: bool = false;

        let target_x: i32 = target[0];
        let target_y: i32 = target[1];
        let target_z: i32 = target[2];

        for triplet in triplets {
            let (i, j, k) = (triplet[0], triplet[1], triplet[2]);

            x |= i == target_x && j <= target_y && k <= target_z;
            y |= i <= target_x && j == target_y && k <= target_z;
            z |= i <= target_x && j <= target_y && k == target_z;
        }

        x && y && z
    }
}
// @lc code=end
