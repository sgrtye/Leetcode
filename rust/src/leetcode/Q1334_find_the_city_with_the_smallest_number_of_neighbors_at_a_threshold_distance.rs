/*
 * @lc app=leetcode id=1334 lang=rust
 *
 * [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
 */

// @lc code=start
impl Solution {
    pub fn find_the_city(n: i32, edges: Vec<Vec<i32>>, distance_threshold: i32) -> i32 {
        let mut dp: Vec<Vec<i32>> = vec![vec![i32::MAX; n as usize]; n as usize];

        for edge in edges {
            let source: usize = edge[0] as usize;
            let target: usize = edge[1] as usize;
            let weight: i32 = edge[2];

            dp[source][target] = weight;
            dp[target][source] = weight;
        }

        for k in 0..n as usize {
            for row in 0..n as usize {
                for col in 0..n as usize {
                    if dp[row][k] != i32::MAX && dp[k][col] != i32::MAX {
                        dp[row][col] = dp[row][col].min(dp[row][k] + dp[k][col]);
                    }
                }
            }
        }

        let mut counts: Vec<i32> = vec![0; n as usize];

        for row in 0..n as usize {
            for col in row + 1..n as usize {
                if dp[row][col] <= distance_threshold {
                    counts[row] += 1;
                    counts[col] += 1;
                }
            }
        }

        let mut result: usize = 0;
        let mut current: i32 = counts[0];

        for i in 1..n as usize {
            if counts[i] <= current {
                result = i;
                current = counts[i];
            }
        }

        result as i32
    }
}
// @lc code=end
