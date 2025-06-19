/*
 * @lc app=leetcode id=435 lang=rust
 *
 * [435] Non-overlapping Intervals
 */

// @lc code=start
impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals: Vec<Vec<i32>> = intervals;
        intervals.sort();

        let mut result: i32 = 0;
        let mut end: i32 = intervals[0][1];

        for i in 1..intervals.len() {
            if intervals[i][0] < end {
                result += 1;
                end = end.min(intervals[i][1]);
            } else {
                end = intervals[i][1];
            }
        }

        result
    }
}
// @lc code=end
