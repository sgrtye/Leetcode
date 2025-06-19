/*
 * @lc app=leetcode id=56 lang=rust
 *
 * [56] Merge Intervals
 */

// @lc code=start
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut intervals: Vec<Vec<i32>> = intervals;
        intervals.sort();

        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut start: i32 = intervals[0][0];
        let mut end: i32 = intervals[0][1];

        for i in 0..intervals.len() {
            end = end.max(intervals[i][1]);

            if i != intervals.len() - 1 && intervals[i + 1][0] <= end {
                continue;
            }

            result.push(vec![start, end]);

            if i != intervals.len() - 1 {
                start = intervals[i + 1][0];
                end = intervals[i + 1][1];
            }
        }

        result
    }
}
// @lc code=end
