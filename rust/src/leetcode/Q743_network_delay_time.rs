/*
 * @lc app=leetcode id=743 lang=rust
 *
 * [743] Network Delay Time
 */

// @lc code=start
use std::collections::BinaryHeap;

impl Solution {
    fn floyd_warshall(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut dp: Vec<Vec<i32>> = vec![vec![i32::MAX; n as usize]; n as usize];
        for t in times {
            let source: usize = t[0] as usize - 1;
            let target: usize = t[1] as usize - 1;
            let time: i32 = t[2];

            dp[source][target] = time;
        }

        for i in 0..n as usize {
            dp[i][i] = 0;
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

        let result: i32 = *dp[k as usize - 1].iter().max().unwrap();

        if result == i32::MAX {
            -1
        } else {
            result
        }
    }

    fn bellman_ford(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut distances: Vec<i32> = vec![i32::MAX; n as usize];
        distances[k as usize - 1] = 0;

        for _ in 0..n - 1 {
            for time in &times {
                if distances[time[0] as usize - 1] != i32::MAX
                    && distances[time[0] as usize - 1] + time[2] < distances[time[1] as usize - 1]
                {
                    distances[time[1] as usize - 1] = distances[time[0] as usize - 1] + time[2];
                }
            }
        }

        let result: i32 = *distances.iter().max().unwrap();

        if result == i32::MAX {
            -1
        } else {
            result
        }
    }

    fn dijkstras(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut adjecent_list: Vec<Vec<(usize, i32)>> = vec![vec![]; n as usize];
        for t in times {
            let source: usize = t[0] as usize - 1;
            let target: usize = t[1] as usize - 1;
            let time: i32 = t[2];

            adjecent_list[source].push((target, time));
        }

        let mut visited: Vec<bool> = vec![false; n as usize];
        let mut distances: Vec<i32> = vec![i32::MAX; n as usize];
        let mut explore: BinaryHeap<(i32, usize)> = BinaryHeap::new();

        explore.push((0, k as usize - 1));

        while !explore.is_empty() {
            let (accumulated_time, vertex) = explore.pop().unwrap();
            if visited[vertex] {
                continue;
            }

            visited[vertex] = true;
            distances[vertex] = -accumulated_time;

            for &(target, time) in &adjecent_list[vertex] {
                if !visited[target] {
                    explore.push((accumulated_time - time, target));
                }
            }
        }

        let result: i32 = *distances.iter().max().unwrap();

        if result == i32::MAX {
            -1
        } else {
            result
        }
    }

    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        Self::dijkstras(times, n, k)
    }
}
// @lc code=end
