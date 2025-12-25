/*
 * @lc app=leetcode id=57 lang=rust
 *
 * [57] Insert Interval
 */

// @lc code=start
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut new_start = new_interval[0];
        let mut new_end = new_interval[1];
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut added: bool = false;

        for interval in intervals {
            if added {
                result.push(interval);
                continue;
            }

            let current_start = interval[0];
            let current_end = interval[1];

            if current_end < new_start {
                result.push(interval);
                continue;
            }

            if new_end < current_start {
                added = true;
                result.extend(vec![vec![new_start, new_end], interval]);
                continue;
            }

            new_start = new_start.min(current_start);
            new_end = new_end.max(current_end);
        }

        if !added {
            result.push(vec![new_start, new_end])
        }

        result
    }
}
// @lc code=end
