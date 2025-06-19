/*
 * @lc app=leetcode id=1851 lang=rust
 *
 * [1851] Minimum Interval to Include Each Query
 */

// @lc code=start
use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::collections::HashMap;

impl Solution {
    pub fn min_interval(intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let mut intervals: Vec<Vec<i32>> = intervals;
        let mut sorted_queries: Vec<i32> = queries.clone();

        intervals.sort();
        sorted_queries.sort();

        let mut current: usize = 0;
        let mut results: HashMap<i32, i32> = HashMap::new();
        let mut min_heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();

        for query in sorted_queries {
            while current < intervals.len() && intervals[current][0] <= query {
                min_heap.push(Reverse((
                    intervals[current][1] - intervals[current][0] + 1,
                    intervals[current][1],
                )));
                current += 1;
            }

            while !min_heap.is_empty() && min_heap.peek().unwrap().0 .1 < query {
                min_heap.pop();
            }

            if !min_heap.is_empty() {
                let Reverse((size, _)) = *min_heap.peek().unwrap();
                results.insert(query, size);
            } else {
                results.insert(query, -1);
            }
        }

        queries.iter().map(|q| *results.get(q).unwrap()).collect()
    }
}
// @lc code=end
