/*
 * @lc app=leetcode id=994 lang=rust
 *
 * [994] Rotting Oranges
 */

// @lc code=start
impl Solution {
    fn elapse(
        grid: &mut Vec<Vec<i32>>,
        fresh_oranges: &mut i32,
        rotten_oranges: &Vec<(i32, i32)>,
    ) -> Vec<(i32, i32)> {
        let mut new_rotten_list: Vec<(i32, i32)> = Vec::new();
        static DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

        for &(row, col) in rotten_oranges {
            for (dx, dy) in DIRECTIONS {
                if row + dx >= 0
                    && col + dy >= 0
                    && row + dx < grid.len() as i32
                    && col + dy < grid[0].len() as i32
                    && grid[(row + dx) as usize][(col + dy) as usize] == 1
                {
                    *fresh_oranges -= 1;
                    new_rotten_list.push(((row + dx), (col + dy)));
                    grid[(row + dx) as usize][(col + dy) as usize] = 2;
                }
            }
        }

        new_rotten_list
    }

    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let mut fresh_oranges: i32 = 0;
        let mut grid: Vec<Vec<i32>> = grid;
        let mut rotten_oranges: Vec<(i32, i32)> = Vec::new();

        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                match grid[i][j] {
                    1 => {
                        fresh_oranges += 1;
                    }
                    2 => {
                        rotten_oranges.push((i as i32, j as i32));
                    }
                    _ => {}
                }
            }
        }

        if fresh_oranges == 0 {
            return 0;
        }

        let mut time: i32 = 0;
        while !rotten_oranges.is_empty() {
            rotten_oranges = Self::elapse(&mut grid, &mut fresh_oranges, &rotten_oranges);
            time += 1;
        }

        if fresh_oranges == 0 {
            time - 1
        } else {
            -1
        }
    }
}
// @lc code=end
