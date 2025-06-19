/*
 * @lc app=leetcode id=778 lang=rust
 *
 * [778] Swim in Rising Water
 */

// @lc code=start
use std::collections::BinaryHeap;

impl Solution {
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let size: usize = grid.len();
        static DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        let mut visited: Vec<bool> = vec![false; size * size];
        let mut explore: BinaryHeap<(i32, i32, i32)> = BinaryHeap::new();

        explore.push((-grid[0][0], 0, 0));

        while !explore.is_empty() {
            let (time, row, col) = explore.pop().unwrap();

            if visited[row as usize * size + col as usize] {
                continue;
            }

            if row == size as i32 - 1 && col == size as i32 - 1 {
                return -time;
            }

            visited[row as usize * size + col as usize] = true;

            for (dx, dy) in DIRECTIONS {
                let new_row: i32 = row + dx;
                let new_col: i32 = col + dy;

                if new_row >= 0
                    && new_col >= 0
                    && new_row < size as i32
                    && new_col < size as i32
                    && !visited[new_row as usize * size + new_col as usize]
                {
                    explore.push((
                        time.min(-grid[new_row as usize][new_col as usize]),
                        new_row,
                        new_col,
                    ));
                }
            }
        }

        -1
    }
}
// @lc code=end
