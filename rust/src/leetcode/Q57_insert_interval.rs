/*
 * @lc app=leetcode id=57 lang=rust
 *
 * [57] Insert Interval
 */

// @lc code=start
use std::cmp::Ordering;

impl Solution {
    fn insert_with_looping(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut interval_start: i32 = new_interval[0];
        let mut interval_end: i32 = new_interval[1];

        for i in 0..intervals.len() {
            if interval_end < intervals[i][0] {
                res.push(vec![interval_start, interval_end]);
                res.extend_from_slice(&intervals[i..]);
                return res;
            } else if interval_start > intervals[i][1] {
                res.push(intervals[i].clone());
            } else {
                interval_start = interval_start.min(intervals[i][0]);
                interval_end = interval_end.max(intervals[i][1]);
            }
        }

        res.push(vec![interval_start, interval_end]);
        res
    }

    fn find_non_overlapping_start(
        intervals: &Vec<Vec<i32>>,
        new_interval: &Vec<i32>,
    ) -> Option<usize> {
        let mut left: usize = 0;
        let mut right: i32 = intervals.len() as i32 - 1;

        let target: i32 = new_interval[0];

        while left as i32 <= right {
            let mid: usize = left + ((right - left as i32) / 2) as usize;

            match intervals[mid][1].cmp(&target) {
                Ordering::Less => left = mid + 1,
                Ordering::Greater => right = mid as i32 - 1,
                Ordering::Equal => right = mid as i32 - 1,
            }
        }

        if right >= 0 {
            Some(right as usize)
        } else {
            None
        }
    }

    fn find_non_overlapping_end(
        intervals: &Vec<Vec<i32>>,
        new_interval: &Vec<i32>,
    ) -> Option<usize> {
        let mut left: i32 = 0;
        let mut right: i32 = intervals.len() as i32 - 1;

        let target: i32 = new_interval[1];

        while left <= right {
            let mid: i32 = left + ((right - left) / 2);

            match intervals[mid as usize][0].cmp(&target) {
                Ordering::Less => left = mid + 1,
                Ordering::Greater => right = mid - 1,
                Ordering::Equal => left = mid + 1,
            }
        }

        if left < intervals.len() as i32 {
            Some(left as usize)
        } else {
            None
        }
    }

    fn insert_by_finding_index(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        if intervals.is_empty() {
            return vec![new_interval];
        }

        let mut new_interval_start: i32 = new_interval[0];
        let mut new_interval_end: i32 = new_interval[1];
        let mut result: Vec<Vec<i32>> = Vec::new();

        if let Some(start) = Self::find_non_overlapping_start(&intervals, &new_interval) {
            if start == intervals.len() - 1 {
                let mut res: Vec<Vec<i32>> = intervals;
                res.push(new_interval);
                return res;
            }

            result.extend_from_slice(&intervals[..=start]);
            new_interval_start = new_interval_start.min(intervals[start + 1][0]);
        } else {
            new_interval_start = new_interval_start.min(intervals[0][0]);
        }

        if let Some(end) = Self::find_non_overlapping_end(&intervals, &new_interval) {
            if end == 0 {
                let mut res: Vec<Vec<i32>> = vec![new_interval];
                res.extend_from_slice(&intervals);
                return res;
            }

            new_interval_end = new_interval_end.max(intervals[end - 1][1]);
            result.push(vec![new_interval_start, new_interval_end]);
            result.extend_from_slice(&intervals[end..]);
        } else {
            new_interval_end = new_interval_end.max(intervals[intervals.len() - 1][1]);
            result.push(vec![new_interval_start, new_interval_end]);
        }

        result
    }

    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        Self::insert_by_finding_index(intervals, new_interval)
    }
}
// @lc code=end
